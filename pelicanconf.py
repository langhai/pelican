#!/usr/bin/env python
# -*- coding: utf-8 -*- #

###Basic Settings####
AUTHOR = u'Hai Lang'
SITENAME = u'Raging Scholars'
SITEURL = 'www.hailang.me'
#SITEURL = '127.0.0.1:8000'
TIMEZONE = 'Asia/Kuala_Lumpur'
DEFAULT_LANG = u'en'
DEFAULT_PAGINATION = 10
###Extra Configurations
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Misc'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
###URL Settings
#ARTICLE_URL = 'posts/{slug}.html'
#ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{category}/{slug}.html'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
###Feed Settings
FEED_DOMAIN = 'http://feed.hailang.me'
###Theme Settings
#THEME = "pelican-chunk"
#THEME = "nmnlist"
THEME = "gum"
###Theme Specific Settings####
DEFAULT_DATE_FORMAT = ('%b %d %Y')
SITESUBTITLE = "uprintf(\'There is no place like ::1\\n\');"
#SINGLE_AUTHOR = False
#MINT = False
DISQUS_SITENAME = 'ragingscholars'
#GOOGLE_ANALYTICS = 'UA-12039368-4'
GOOGLE_ANALYTICS_ID = 'UA-12039368-4'
GOOGLE_ANALYTICS_SITENAME = 'hailang.me'
###Social Settings####
SINA_URL = 'http://www.weibo.com/bestwc'
GITHUB_URL = 'https://github.com/langhai'
TWITTER_URL = 'https://twitter.com/lang_hai'
FACEBOOK_URL = 'http://www.facebook.com/bestwc'
GOOGLEPLUS_URL = 'https://plus.google.com/100640905756801185675/posts/p/pub'

###Not Sure...####
## Blogroll
#LINKS =  (
#            ('FreeBSD Project', 'http://freebsd.org'),
#            ('Google', 'http://google.com'),
#         )
## Social widget
#SOCIAL = (
#            ('Facebook', 'http://www.facebook.com/bestwc'),
#        )



