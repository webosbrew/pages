#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'webosbrew.org'
SITENAME = 'webOS Homebrew Project'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['extra/CNAME']
PAGE_PATHS = ['pages']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Home', '/'),
    ('Repo', 'https://repo.webosbrew.org'),
)

# Blogroll
LINKS = (
    ('webOS Homebrew', 'https://github.com/webosbrew/'),
    ('openlgtv', 'https://openlgtv.github.io/'),
)

# Social widget
SOCIAL = (
    ('openlgtv Discord', 'https://discord.gg/xWqRVEm'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True