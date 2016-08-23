#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Stevie Poppe'
SITENAME = 'Onoreto'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Europe/Paris'
DISPLAY_PAGES_ON_MENU = 'True'
DEFAULT_LANG = 'en'

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#SITE_THUMBNAIL = "/images/pp-thumbnail-small.png"
SITE_THUMBNAIL = "logo2.png"

# NEST Template
THEME = 'nest'
SITESUBTITLE = u'@Stevie Poppe'
# Minified CSS
NEST_CSS_MINIFY = True
# Add items to top menu before pages
MENUITEMS = [('Blog', '/'),('Categories','/blog/category')]
# Add header background image from content/images : 'background.jpg'
NEST_HEADER_IMAGES = ''
NEST_HEADER_LOGO = '/image/logo.png'
# Footer
NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Home','/'),('Archives','/blog/archives'),('Tagcloud','/blog/tags')]
NEST_COPYRIGHT = u'&copy; Stevie Poppe 2016'
# archives.html
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category'

# tag.html
NEST_TAG_HEAD_TITLE = u'Tag'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# # period_archives.html
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# # tags.html
NEST_TAGS_CONTENT_TITLE = u'Tagcloud'
NEST_TAGS_CONTENT_LIST = u'tagged'
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_INDEX_HEAD_TITLE = u'Home'

# search.html
SEARCH_HEAD_TITLE = u'Search'

# Static files
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico', 'extra/logo.svg', 'files']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/logo.svg': {'path': 'logo.svg'}
}

#TEMPLATE_PAGES = {'src/aboutme.html': 'pages/aboutme.html'}
RELATED_POSTS_MAX = 5

TIPUE_SEARCH = 'true'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['tipue_search', 'gzip_cache', "better_figures_and_images",'extract_toc',
'related_posts',"tag_cloud",'pin_to_top','summary','assets']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', 'sitemap'))
SITEMAP_SAVE_AS = 'sitemap.xml'
MD_EXTENSIONS = ['codehilite','extra','smarty', 'toc']
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
#AUTHOR_FEED_ATOM = None
#AUTHOR_FEED_RSS = None

FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'

#FEED_DOMAIN = SITEURL
FEED_DOMAIN = 'https://steviepoppe.github.io'
#SITEURL = 'https://steviepoppe.github.io'
#SITEURL = 'localhost:8000'

SUMMARY_MAX_LENGTH = 512
SUMMARY_USE_FIRST_PARAGRAPH = True

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/PoppeStevie'),
          ('Linkedin', 'https://be.linkedin.com/in/stevie-poppe-9048b395'),
          ('Instagram', 'https://www.instagram.com/stevie.poppe/'),
          ('Goodreads', 'https://www.goodreads.com/user/show/35676792-stevie-poppe'))

GZIP_CACHE = True
#DISQUS_SITENAME = 'steviepoppe'

#GOOGLE_ANALYTICS = 'UA-82857115-1'
RESPONSIVE_IMAGES = True

#ARTICLE_URL = 'blog/{slug}'
#ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"

ARCHIVES_URL = 'blog/archives'
ARCHIVES_SAVE_AS = 'blog/archives/index.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

TAGS_URL = 'blog/tags'
TAGS_SAVE_AS = 'blog/tags/index.html'

TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'

CATEGORY_URL = 'blog/category/{slug}'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
CATEGORIES_URL = 'blog/category'
CATEGORIES_SAVE_AS = 'blog/category/index.html'


#SEARCH_URL = 'search'
#SEARCH_SAVE_AS = 'search.html'

#INDEX_URL = 'blog'
#INDEX_SAVE_AS = "blog/index.html"

TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True