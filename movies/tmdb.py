#!/usr/bin/env python

from config import apiKeys

from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import set_locale

set_key(apiKeys['tmdb'])
set_cache('null')
set_locale('en', 'gb')

