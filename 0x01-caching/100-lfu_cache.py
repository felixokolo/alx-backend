#!/usr/bin/python3
"""
MRU Caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    MRU caching class
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()
        self.__used = {}

    def put(self, key, item):
        """
        Add data to cache
        """
        if key is None or item is None:
            return
        if key in list(self.__used.keys()):
            del self.__used[key]
        try:
            k = min(list(self.__used.values()))
            k = list(self.__used.values()).index(k)
            k = list(self.__used.keys())[k]
        except(Exception):
            k = None
        self.cache_data[key] = item
        self.__used[key] = 0
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(k))
            del self.cache_data[k]
            del self.__used[k]

    def get(self, key):
        """
        Gets data from cache
        """
        if key is None:
            return
        ret = self.cache_data.get(key)
        if ret is not None:
            self.__used[key] += 1
        return ret
