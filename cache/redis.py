import redis
from .settings import REDIS_DB, REDIS_HOST, REDIS_PORT

client = redis.Redis(host=REDIS_DB, port=REDIS_PORT, db=REDIS_DB)