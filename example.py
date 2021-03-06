from ffcache import FirefoxCache, FirefoxCacheEntry
from ffcache.helper import save
import urllib.parse
import os
import brotli
import gzip
import zlib
import sys

cache_dir = os.environ['FFCACHE_DIR']
out_dir = 'tmp'

if not os.path.exists(out_dir):
    os.mkdir(out_dir)

cache: FirefoxCache = FirefoxCache(cache_dir)

entry: FirefoxCacheEntry
for entry in cache.records:
    url = entry.key
    print(url)

    filename = urllib.parse.quote(url, safe='')[:255]
    out_path = os.path.join(out_dir, filename)

    try:
        save(entry, out_path)
    except:
        pass
