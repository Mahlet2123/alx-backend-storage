#!/usr/bin/env python3
""" exercise.py module """
import uuid
import redis
from typing import Union


class Cache():
    """ Cache class """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None):
        value = self._redis.get(key)
        if value:
            if fn:
                value = fn(value)
        else:
            return None
        return value

    def get_str(self, key: str):
        return self.get(key, decode_key())

    def get_int(self):
        return self.get(key, int())

    @staticmethod
    def decode_key(value: bytes) -> str:
        return value.decode("utf8")
