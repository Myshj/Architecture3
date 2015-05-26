# coding=utf-8
__author__ = 'Alexey'

from MockRedis.MockRedisLock import MockRedisLock
from MockRedis.MockRedisPipeline import MockRedisPipeline


class MockRedis(object):
    """Imitate a Redis object so unit tests can run on our Hudson CI server without needing a real
    Redis server."""

    # The 'Redis' store
    redis = {}

    def __init__(self, host, port, db):
        """Initialize the object."""
        print("MockRedis started!")
        pass

    def delete(self, key):  # pylint: disable=R0201
        """Emulate delete."""

        if key in MockRedis.redis:
            del MockRedis.redis[key]

    def exists(self, key):  # pylint: disable=R0201
        """Emulate get."""

        return key in MockRedis.redis

    def flushdb(self):
        """
        Emulate flushdb.
        :return:
        """
        MockRedis.redis.clear()

    def save(self):
        pass

    def incr(self, key, value=1):
        MockRedis.redis[key] += value
        return MockRedis.redis[key]

    def decr(self, key, value=1):
        MockRedis.redis[key] -= value
        return MockRedis.redis[key]

    def get(self, key):  # pylint: disable=R0201
        """Emulate get."""
        print("MockGet")

        # Override the default dict
        result = None if key not in MockRedis.redis else MockRedis.redis[key]
        return result

    def set(self, key, value):
        """
        Emulate set.
        :param key:
        :param value:
        :return:
        """
        MockRedis.redis[key] = value

    def hget(self, hashkey, attribute):  # pylint: disable=R0201
        """Emulate hget."""

        # Return '' if the attribute does not exist
        result = MockRedis.redis[hashkey][attribute] if attribute in MockRedis.redis[hashkey] \
                 else ''
        return result

    def hgetall(self, hashkey):  # pylint: disable=R0201
        """Emulate hgetall."""

        return MockRedis.redis[hashkey]

    def hlen(self, hashkey):  # pylint: disable=R0201
        """Emulate hlen."""

        return len(MockRedis.redis[hashkey])

    def hmset(self, hashkey, value):  # pylint: disable=R0201
        """Emulate hmset."""

        # Iterate over every key:value in the value argument.
        for attributekey, attributevalue in value.items():
            MockRedis.redis[hashkey][attributekey] = attributevalue

    def hset(self, hashkey, attribute, value):  # pylint: disable=R0201
        """Emulate hset."""

        MockRedis.redis[hashkey][attribute] = value

    def keys(self, pattern):  # pylint: disable=R0201
        """Emulate keys."""
        import re

        # Make a regex out of pattern. The only special matching character we look for is '*'
        regex = '^' + pattern.replace('*', '.*') + '$'

        # Find every key that matches the pattern
        result = [key for key in MockRedis.redis.keys() if re.match(regex, key)]

        return result

    def lock(self, key, timeout=0, sleep=0):  # pylint: disable=W0613
        """Emulate lock."""

        return MockRedisLock(self, key)

    def pipeline(self):
        """Emulate a redis-python pipeline."""

        return MockRedisPipeline(self)

    def sadd(self, key, value):  # pylint: disable=R0201
        """Emulate sadd."""

        # Does the set at this key already exist?
        if key in MockRedis.redis:
            # Yes, add this to the set
            MockRedis.redis[key].add(value)
        else:
            # No, override the defaultdict's default and create the set
            MockRedis.redis[key] = set([value])

    def srem(self, key, value):
        """Emulate srem"""

        MockRedis.redis[key]

    def smembers(self, key):  # pylint: disable=R0201
        """Emulate smembers."""

        return MockRedis.redis[key]