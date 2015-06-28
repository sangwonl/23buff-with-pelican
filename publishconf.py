#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DELETE_OUTPUT_DIRECTORY = False

AUTHOR = u'23BUFF'
SITENAME = u'23BUFF'
SITEURL = '23buff.github.io'
TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = u'en'
LOAD_CONTENT_CACHE = False

PATH = 'content'
THEME = './themes/23buff'
THEME_STATIC_DIR = 'theme'
THEME_STATIC_PATHS = ['static']
CSS_FILE = 'main.css'

FACEBOOK_APP_ID = '453239584841665'
GOOGLE_ANALYTICS = 'UA-XXXX-YYYY'