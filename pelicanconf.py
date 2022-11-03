#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = 'Editor'
SITENAME = 'Etched Press'
SITEURL = 'https://etchedpress.com'
GOOGLE_ANALYTICS = 'UA-40679562-1'
GOOGLE_SITE_VERIFICATION = ''

PATH = 'content'
# Static Paths
STATIC_PATHS = ['static', 'static/images', 'static/css', 'wp-content', 'wp-content/uploads', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 
						'extra/favicon.ico': {'path': 'favicon.ico'}}


# Theme Settings
THEME = 'themes/blue-penguin'

DISPLAY_HEADER = True
DISPLAY_FOOTER = False
DISPLAY_HOME   = True
DISPLAY_MENU   = True



## Path to favicon
FAVICON = 'static/images/favicon.ico'

## Path to logo for nav menu (optional)
LOGO = 'static/images/logo.png'

SITEDESCRIPTION = 'Etched Press, based in San Franciso, founded in Wilmington, North Carolina is a micro press that publishes chapbooks of poetry and anthologies.'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Make into Static Site with Secondary Blog
ARTICLE_PATHS = ['shop']
ARTICLE_URL = 'shop/{slug}.html'
ARTICLE_SAVE_AS = 'shop/{slug}.html'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = 'shop/category/{slug}.html'
CATEGORY_URL = 'shop/category/{slug}.html'
TAG_SAVE_AS = 'shop/tag/{slug}.html'
TAG_URL = 'shop/tag/{slug}.html'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False


# Plugins Settings
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


# Blogroll
LINKS = (('The Living Room', 'https://thelivingroomsf.com'),
         ('Syzygy SF', 'https://syzygysf.com/'),
         )

# Social widget
SOCIAL = (('facebook', 'https://www.facebook.com/etchedpress/'),
          ('twitter', 'https://twitter.com/etchedpress/'),
          )

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Turn off caching for local development
LOAD_CONTENT_CACHE = False
