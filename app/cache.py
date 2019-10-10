from flask_caching import Cache
from app.config import Config

cache_servers = Config.cache_servers

cache = Cache(config={
    'CACHE_TYPE': 'memcached',
    'CACHE_DEFAULT_TIMEOUT': 0,
    'CACHE_MEMCACHED_SERVERS': cache_servers
})