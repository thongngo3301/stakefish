import redis
import os

# Initialize Redis client
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db = int(os.getenv('REDIS_DB', 0))

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)
