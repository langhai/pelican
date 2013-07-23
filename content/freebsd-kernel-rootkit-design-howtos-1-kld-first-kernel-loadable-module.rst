FreeBSD Kernel Rootkit Design Howtos 1 KLD First Kernel Loadable Module
#######################################################################

:date: 16-04-2013
:tags: rootkit, freebsd
:category: Code!
:slug: freebsd-kernel-rootkit-design-howtos-1-kld-first-kernel-loadable-module
:author: Hai Lang
:status: draft

Needless to say that the first thing you need to start FreeBSD kernel rootkit development is a FreeBSD box. 
There are plenty of installation guides on the Internet about FreeBSD installation, 
so that I'll just skip this part for the sake of simplicity.

And FYI, basically you are free to choose any hardware to run FreeBSD as long as it's supported. 
You can even install your FreeBSD as a virtual machine. 
10GB hard drive, at least 512MB memory with any modern CPU will do.

The Environment
------------------
The version of FreeBSD I'm going to use throughout this howtos is FreeBSD 9 Stable, 
it is recommended that you install at least FreeBSD 9 Release although I believe code examples in this howtos 
are able to run on most of versions after FreeBSD 6.2

.. code-block:: bash

    myBSD# uname -a
    FreeBSD myBSD 9.0-STABLE FreeBSD 9.0-STABLE #0: Thu Mar  8 14:16:25 CST 2012 bestwc@myBSD:/usr/obj/usr/src/sys/GENERIC  amd64

Package Installation
--------------------
You'll need the FreeBSD source tree to compile your kernel rootkit, 
be sure to install it because it is not included in minimal installation. 
You can do this by two ways, the first is to enable src distribution option during installation, 
and the recommended way is to perform the following command.

.. code-block:: bash

    myBSD# cp /usr/share/examples/cvsup/stable-supfile /root && cd /root
    myBSD# ee stable-supfile
    =================================
    *default host=CHANGE_THIS.FreeBSD.org ###Change this line
    *default host=cvsup.FreeBSD.org ###To this
    =================================
    myBSD# csup -g -L2 stable-supfile

This will sync the source tree on your local file system to the latest one from remote repository, 
and this will simply download the latest for you if you don't already have the source tree. 
It is recommended to run the cusp command shown above to frequently update your source tree, 
for this will make sure your are developing rootkit with the newest kernel source code, 
and potentially make it more compatible with new FreeBSD releases.

To examine if you have the src tree on your local box, type the following command:

.. code-block:: bash

    myBSD# ls /usr/src
    COPYRIGHT       ObsoleteFiles.inc       crypto          lib         share
    LOCKS           README      etc         libexec         sys
    MAINTAINERS     UPDATING    games       release         tools
    Makefile        bin         gnu         rescue          usr.bin
    Makefile.inc1   cddl        include     sbin            usr.sbin
    Makefile.mips   contrib     kerberos5   secure

The Dynamic Kernel Linker (KLD)
-------------------------------
The Dynamic Kernel Linker (KLD) is a facility in FreeBSD that allows users 
to interact with the system kernel by dynamically loading or unloading kernel modules. 
It may sounds strange to you, but believe it or not that you have utilized KLD multiple times 
during daily operations on your FreeBSD box. The KLD gets called every time you plug in or plug out a device, 
or by manually typing kldload or kldunload commands. 
It is especially useful to device driver developers as they can dynamically load 
their drivers as kernel module and test the functionalities on the fly without rebooting the system. 
For more information on the KLD, please refer to the `FreeBSD Handbook`_

The KLD provides a high way for us to put our code into the running kernel space 
without recompiling as long as we have the required privilege. 
So that, if we have our kernel rootkit compiled as loadable kernel module, 
then we'll theoretically be able to load that module in any FreeBSD machines on the fly.

Although the KLD interface is not the only way for people to interact with kernel, 
but is undoubtedly the easiest and probably the fastest way to do that. 
The only question is, will there be any compatibility issues if we stick to KLD interface?

.. pull-quote:: In FreeBSD 3.0, substantial changes were made to the kernel module subsystem, and the LKM Facility was renamed the Dynamic Kernel Linker (KLD) Facility. Subsequently, the term KLD is commonly used to describe LKMs under FreeBSD.

According to the quote above from `Designing BSD Rootkits: An Introduction to Kernel Hacking`_ by Joseph Kong, 
the KLD interface hasn't been changed since FreeBSD 3.0, 
which means our yet-to-be-done rootkit should be able to run on any (not always true) modern FreeBSD systems 
without any (not always true as well) modification.

Just incase that you haven't realized this, 
**we are going to use KLD interfaces a lot in this tutorial.** 
Now let's get to know the KLD interface more.

The Module Event Handler
------------------------------
When you load or unload any kernel modules to or from the current running kernel, 
the KLD interface will perform some pre-defined routines to prepare the system. 
This is called the Module Event Handler, it should be present in every(!) kernel module 
to handle the initialization and shutdown processes. This handler gets called every time 
when the code enters or exits kernel space.

(!) Just keep in mind that this isn't always true, as what the quote says below from 
`Designing BSD Rootkits: An Introduction to Kernel Hacking`_

.. pull-quote:: Actually, this isn't entirely true. You can have a KLD that just includes a sysctl. You can also dispense with module handlers if you wish and just use SYSINIT and SYSUNINIT directly to register functions to be invoked on load and unload, respectively. You can't, however, indicate failure in those.

The prototype of the module event handler is defined in sys/module.h and it is called modeventhand_t

.. code-block:: cpp

    FILE:/usr/src/sys/sys/module.h

    myBSD# cat /usr/src/sys/sys/module.h | grep modeventhand_t
    typedef int (*modeventhand_t)(module_t, int /* modeventtype_t */, void *);

The module_t is a pointer to the module\u2019s struct as defined in the same file.

.. code-block:: cpp

    FILE:/usr/src/sys/sys/module.h

    typedef struct module *module_t;

The modeventtype_t on the other hand is an enumerated type of event types defined in the same file as well.

.. code-block:: cpp

    FILE:/usr/src/sys/sys/module.h
    
    typedef enum modeventtype {
            MOD_LOAD,    /* Set when module is loaded. */
            MOD_UNLOAD,    /* Set when module is unloaded. */
            MOD_SHUTDOWN,    /* Set on shutdown. */
            MOD_QUIESCE    /* Set on quiesce. */
    } modeventtype_t;

With all these information, we can now try to define a simple module event handler. 
Here is a simple event handler function called load, which displays Hello, world! when it's loaded, 
and print Good-bye, cruel world! when it's unloaded.

.. code-block:: cpp

    static int load(struct module *module, int cmd, void *arg)
    {
        int error = 0;

        switch (cmd) {
        case MOD_LOAD:
            uprintf("Hello, world!\n");
            break;

        case MOD_UNLOAD:
            uprintf("Good-bye, cruel world!\n");
        break;

        default:
            error = EOPNOTSUPP; //EOPNOTSUPP stands for Error: Operation not supported.
            break;
        }

        return(error);
    }

It's perfectly safe if this code doesn't make much sense to you, as we will get back later. 
However, what you do need to understand is the prototype of defining a module event handler.

This code snippet should present in your first loadable kernel module, 
and perform pre-defined routines according to the cmd sent by the kernel accordingly.

Consider this to be a protocol between your module and the kernel, 
which basically says 
**"Oh the user asked you to unload me? Hold on and let me check my event handler, 
alright, I'll print Good-bye, cruel world! and then go away."**

The DECLARE_MODULE Macro
---------------------------
It's time to get back to our module declaration.

We now know module_t is a pointer to the module structure, 
but what on earth is a module and how do we define it? 
The thing is, we must let KLD know the basic information about our module, 
and it should register itself with kernel when it loads. 
This process can be awfully long and complicated, 
lucky that we have a pre-defined macro in sys/module.h that just does this to help us.

.. _FreeBSD Handbook: http://www.freebsd.org/doc/en/books/arch-handbook/driverbasics-kld.html
.. _Designing BSD Rootkits\: An Introduction to Kernel Hacking: http://www.amazon.com/gp/product/B002MZAR6I/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=imhala-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B002MZAR6I
