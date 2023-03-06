#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import datetime

AUTHOR = 'webosbrew.org'
SITENAME = 'webOS Homebrew Project'
SITEURL = ''
SOURCEURL = 'https://github.com/webosbrew/webosbrew.github.io/blob/main/content'

THEME = 'webosbrew'
WEBASSETS_SOURCE_PATHS = ['static']

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
    ("Applications", "https://repo.webosbrew.org"),
    ("Develop", "/develop/"),
)

LINKS = (
    ('Github Organization', 'https://github.com/webosbrew/'),
    ('Join us on Discord', 'https://discord.gg/xWqRVEm'),
    ('RootMy.TV', 'https://rootmy.tv/'),
    ('openlgtv', 'https://openlgtv.github.io/'),
)

DEFAULT_PAGINATION = 10

PATH_METADATA = "pages/(?P<path_no_ext>.*)\..*"

ARTICLE_URL = PAGE_URL = "{path_no_ext}/"
ARTICLE_SAVE_AS = PAGE_SAVE_AS = "{path_no_ext}/index.html"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

COPYRIGHT_YEAR = datetime.date.today().year

ENABLE_SEARCH = True
SEARCH_HTML_SELECTOR = "div.main"
