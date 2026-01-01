from redis import Redis
from rq import Queue

redis_conn = Redis(host="localhost", port=6379, decode_responses=True)

queue = Queue("rag-queue", connection=redis_conn)
