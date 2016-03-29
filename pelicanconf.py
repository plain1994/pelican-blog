#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

DIRECT_TEMPLATES = (('search',))

AUTHOR = u'Yuchuan Gou'
SITENAME = u"tomgou.xyz"
SITEURL = 'http://blog.tomgou.xyz'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'ch'

THEME = 'pelican-bootstrap3'
#DISQUS_SITENAME = "Tom's Blog"
DUOSHUO_SITENAME = "blog.tomgou.xyz"

OUTPUT_PATH = './output'
#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把index.html上传到repo的master分支的根目录才可以!
DEFAULT_CATEGORY ='Blogs'

GOOGLE_ANALYTICS = 'UA-74218843-1'#谷歌站点分析


#DISPLAY_RECENT_POSTS_ON_SIDEBAR = True


GITHUB_USER = "plain1994"
GITHUB_REPO_COUNT  = 3

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tag_cloud","sitemap","tipue_search"]


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'daily'
    }
}


TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True

#BOOTSTRAP_FLUID = True
#DISPLAY_CATEGORY_IN_BREADCRUMBS = True
BOOTSTRAP_NAVBAR_INVERSE = True
FAVICON = 'images/carrot.jpg'
#AVATAR = 'images/gou.jpeg'
#ABOUT_ME = 'A student at SJTU'

BANNER = 'images/saul.jpg'
BANNER_COMMENT = 'blog.tomgou.xyz'
#BANNER_SUBTITLE = 'This is my subtitle'

#ADDTHIS_PROFILE = 'plain1994'
#add addthis in duoshuo comment
#add revolvermaps in sidebar.html

#DISPLAY_ARTICLE_INFO_ON_INDEX = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
       )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/plain1994'),
          ('weibo', 'http://weibo.com/tomgou'),
          ('facebook', 'http://www.facebook.com/yuchuangou'),
          )

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
