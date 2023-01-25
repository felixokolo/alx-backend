#!/usr/bin/python3
"""
Basic Caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching class
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()

    def put(self, key, item):
        """
        Add data to cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets data from cache
        """
        if key is None:
            return
        return self.cache_data.get(key)
