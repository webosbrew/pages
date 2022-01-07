#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'webosbrew.org'
SITENAME = 'webOS Homebrew Project'
SITEURL = ''

THEME = './theme'
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['assets']
ASSET_SOURCE_PATHS = ['static']

PATH = 'content'

STATIC_PATHS = ['extra/CNAME']
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False

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
    ('Applications', 'https://repo.webosbrew.org'),
    ('Develop', '/develop'),
)

# Blogroll
LINKS = (
    ('webOS Homebrew', 'https://github.com/webosbrew/'),
    ('openlgtv', 'https://openlgtv.github.io/'),
    ('openlgtv Discord', 'https://discord.gg/xWqRVEm'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
