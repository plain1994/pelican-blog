#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tom Gou'
SITENAME = u"Tom Gou's Blog"
SITEURL = ''

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

#TAG_CLOUD_STEPS = 4
#TAG_CLOUD_MAX_ITEMS = 100
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True


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

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
