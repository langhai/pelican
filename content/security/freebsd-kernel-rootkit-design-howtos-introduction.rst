FreeBSD Kernel Rootkit Design Howtos - Introduction
###################################################

:date: 16-04-2013
:tags: security, rootkit, freebsd
:category: Security!
:slug: freebsd-kernel-rootkit-design-howtos-introduction
:author: Hai Lang
:status: published

Background
--------------
I actually wanted to write this howto together with my college final year project synchronously, 
but sadly things didn't work out the way i expected. 
It took me almost a year to reach this point of rewriting most of them to make them more like tutorials 
other than academic class notes.

Anyway, here I am, writing this intro again, hoping that I can finally finish it sometime soon.

As I said that FreeBSD Kernel Rootkit Design and Defense Techniques is the title of my college final year project,
I chose this topic because my lecturer who I consulted with obviously thinks this one can help me 
at applying master degree in malicious software analysis.

I myself have no interest in pursuing master degree in malicious software analysis, 
but it sure sounds cool to me to create my very own rootkit, especially on my favorite platform, FreeBSD.

I still remember the lecturer asked me why I wanna make it on FreeBSD instead of Linux, 
well, there are two reasons.

* I'm more familiar with FreeBSD than Linux
* I don't see any recent and public accessible rootkit for FreeBSD

Furthermore, there is another secret weapon to make my life even easier, 
`Designing BSD Rootkits: An Introduction to Kernel Hacking`_ by Joseph Kong. 
I highly recommend you guys to grab a copy of this book. 
It's good, and it's the only book on FreeBSD kernel rootkit design as far as I know, 
so you kinda have no choice here.

There's another nice book to start with, 
`The Design and Implementation of the FreeBSD Operating System`_ By Marshall Kirk McKusick and George V. Neville-Neil. 
As the book name suggests, it can give you a detailed understanding of FreeBSD kernel. 
Get a copy of this book, read the first few chapters to get a rough understanding 
and use it as a reference book later on when you work on specific modules of the kernel.

What to Expect
------------------
`Designing BSD Rootkits: An Introduction to Kernel Hacking`_ by Joseph Kong 
is somehow sufficient for lots of people to kickstart their own rootkit, 
but you have to be familiar with modern system kernels and have some experiences in working in C.

I find this book a little bit rushy, what the author did was to drag you through lots of kernel terminologies 
and then give you lots of code snippets that, I myself at least, couldn't understand until 
read them for multiple times.

`The Design and Implementation of the FreeBSD Operating System`_ By Marshall Kirk McKusick and George V. Neville-Neil 
on the other hand, discusses overall FreeBSD kernel implementation and as well as each major kernel modules 
in detail, but the only drawback is that it doesn't talk much about rootkit techniques, 
it only concentrates on normal kernel development.

So that's why I wrote this series on FreeBSD Kernel Rootkit Design, 
it combines what I have learned, and what I think is useful from all those books and online resources. 
I also improved some of the examples from Joseph Kong's book, 
filled in all related information which were omitted by the author.

Consider this as a tutorial series. If you are looking for a quick and comprehensive 
from novice to advanced novice guide on writing FreeBSD Kernel Rookits, then congratulations, 
this is just right for you.

Table of Contents
------------------
Here's a list of the tutorials, feel free to jump to any one that interests you.

* `FreeBSD Kernel Rootkit Design Howtos 1 KLD First Kernel Loadable Module`_
* `FreeBSD Kernel Rootkit Design Howtos 2 System Call First Kernel Service Module`_
* `FreeBSD Kernel Rootkit Design Howtos 3 System Call First Kernel Service Application`_
* `FreeBSD Kernel Rootkit Design Howtos 4 Kerenl and User Space Transitions`_
* `FreeBSD Kernel Rootkit Design Howtos 5 Character Device First cdev Modlue`_
* `FreeBSD Kernel Rootkit Design Howtos 6 Character Device First cdev Application`_
* `FreeBSD Kernel Rootkit Design Howtos 7 Linker Files and Chapter Summary`_
* `FreeBSD Kernel Rootkit Design Howtos 8 System Call Hook and mkdir_hook Example`_
* `FreeBSD Kernel Rootkit Design Howtos 9 Hook Kernel Process Tracking and rmdir_hook Example`_

.. _Designing BSD Rootkits\: An Introduction to Kernel Hacking: http://www.amazon.com/gp/product/B002MZAR6I/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=imhala-20&linkCode=as2&camp=217145&creative=399373&creativeASIN=B002MZAR6I
.. _The Design and Implementation of the FreeBSD Operating System: http://www.amazon.com/gp/product/0201702452/ref=as_li_qf_sp_asin_tl?ie=UTF8&tag=imhala-20&linkCode=as2&camp=1789&creative=9325&creativeASIN=0201702452
.. _FreeBSD Kernel Rootkit Design Howtos 1 KLD First Kernel Loadable Module: http://old.hailang.me/2012/06/08/freebsd-kernel-rootkit-design-howtos---1---kld-first-kernel-loadable-module/
.. _FreeBSD Kernel Rootkit Design Howtos 2 System Call First Kernel Service Module: http://old.hailang.me/2012/06/09/freebsd-kernel-rootkit-design-howtos---2---system-call-first-kernel-service-module/
.. _FreeBSD Kernel Rootkit Design Howtos 3 System Call First Kernel Service Application: http://old.hailang.me/2012/06/09/freebsd-kernel-rootkit-design-howtos---3---system-call-first-kernel-service-application/http://old.hailang.me/2012/06/09/freebsd-kernel-rootkit-design-howtos---3---system-call-first-kernel-service-application/
.. _FreeBSD Kernel Rootkit Design Howtos 4 Kerenl and User Space Transitions: http://old.hailang.me/2012/06/10/freebsd-kernel-rootkit-design-howtos---4---kernel-and-user-space-transitions/
.. _FreeBSD Kernel Rootkit Design Howtos 5 Character Device First cdev Modlue: http://old.hailang.me/2012/06/19/freebsd-kernel-rootkit-design-howtos---5---character-device-first-cdev-module/
.. _FreeBSD Kernel Rootkit Design Howtos 6 Character Device First cdev Application: #
.. _FreeBSD Kernel Rootkit Design Howtos 7 Linker Files and Chapter Summary: #
.. _FreeBSD Kernel Rootkit Design Howtos 8 System Call Hook and mkdir_hook Example: #
.. _FreeBSD Kernel Rootkit Design Howtos 9 Hook Kernel Process Tracking and rmdir_hook Example: #
