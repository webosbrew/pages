#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'webosbrew.org'
SITENAME = 'webOS Homebrew Project'
SITEURL = ''

THEME = './theme'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']
ASSET_SOURCE_PATHS = ['static']

PATH = 'content'

STATIC_PATHS = ['extra/CNAME']
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'anchorlink': False,
            'permalink': True,
        },
    },
    'output_format': 'html5',
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
    ('Github Organization', 'https://github.com/webosbrew/'),
    ('Join us on Discord', 'https://discord.gg/xWqRVEm'),
    ('RootMy.TV', 'https://rootmy.tv/'),
    ('openlgtv', 'https://openlgtv.github.io/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

COPYRIGHT_YEAR = datetime.date.today().year
