#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

import pelican.themes.webosbrew
from pelican.plugins import webassets
from webassets.cache import MemoryCache

AUTHOR = 'webosbrew.org'
SITENAME = 'webOS Homebrew Project'
SITEURL = ''
SOURCEURL = 'https://github.com/webosbrew/webosbrew.github.io/blob/main/content'

THEME = 'webosbrew'
THEME_STATIC_PATHS = [pelican.themes.webosbrew.static_dir()]
WEBASSETS_SOURCE_PATHS = [pelican.themes.webosbrew.scss_dir()]

PLUGINS = [webassets]

WEBASSETS_CONFIG = [
    ("CACHE", MemoryCache(1024)),
    ("PYSCSS_LOAD_PATHS", [pelican.themes.webosbrew.scss_dir()]),
]

PATH = 'content'

STATIC_PATHS = ['extra/CNAME']
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = False

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
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
