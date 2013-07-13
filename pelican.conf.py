#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Multiple'
SITENAME = u'Nairobi GNU/Linux Users Group'
SITEURL = 'http://nairobilug.github.io/nairobilug.or.ke'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_PERMALINK_STRUCTURE = '/%Y/%m/'

# copy CNAME to output root
FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
)

GITHUB_URL = 'http://github.com/nairobilug/'
