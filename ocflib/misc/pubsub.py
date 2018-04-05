import redis
import functools

get_redis_connection = functools.partial(redis.StrictRedis,
                                        host='broker',
                                        port=6379,
                                        db=0,
                                        password=None
                                        )

def publish(host, password, channel, message):
    rc = get_redis_connection(host=host, password=password) 
    rc.publish(channel, message)

def subscribe(host, password, *channels):
    rc = get_redis_connection(host=host, password=password)
    sub = rc.pubsub()
    sub.subscribe(channel for channel in channels)
    return sub
