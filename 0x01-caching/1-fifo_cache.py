#!/usr/bin/python3
"""
FIFO Caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching class
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
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            k = list(self.cache_data.keys())[0]
            print('DISCARD:{}'.format(k))
            del self.cache_data[k]

    def get(self, key):
        """
        Gets data from cache
        """
        if key is None:
            return
        return self.cache_data.get(key)
