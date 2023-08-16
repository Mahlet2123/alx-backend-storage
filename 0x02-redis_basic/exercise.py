#!/usr/bin/env python3
""" exercise.py module """
import uuid
import redis
from typing import Union


class Cache():
    """ Cache class """
    def __init__(self):
        """ constructor method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key (e.g. using uuid),
        store the input data in Redis using the random key
        and return the key. """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
            self,
            key: str, fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float]:
        """ get value from redis """
        value = self._redis.get(key)
        if value:
            if fn:
                value = fn(value)
        else:
            return None
        return value

    def get_str(self, key: str) -> str:
        """
        convert redis return value to string
        return self.get(key, fn=lambda d: d.decode("utf-8"))
        """
        return self.get(key, decode_key())

    def get_int(self, key: str) -> int:
        """ convert redis return value into int """
        return self.get(key, int())

    @staticmethod
    def decode_key(value: bytes) -> str:
        """ decode_key static method """
        return value.decode("utf8")
