#!/usr/bin/python3
"""
LRU Caching class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRU caching class
    """

    def __init__(self):
        """
        Initialization
        """
        super().__init__()
        self.__age = 0
        self.__used = {}

    def put(self, key, item):
        """
        Add data to cache
        """
        if key is None or item is None:
            return
        if key in list(self.__used.values()):
            k = list(self.__used.values()).index(key)
            k = list(self.__used.keys())[k]
            del self.__used[k]
        try:
            k = min(list(self.__used.keys()))
        except(Exception):
            k = None
        self.cache_data[key] = item
        self.__used[self.__age] = key
        self.__age += 1
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD: {}'.format(self.__used[k]))
            del self.cache_data[self.__used[k]]
            del self.__used[k]

    def get(self, key):
        """
        Gets data from cache
        """
        if key is None:
            return
        try:
            age = list(self.__used.values()).index(key)
            age = list(self.__used.keys())[age]
            del self.__used[age]
        except(Exception):
            pass
        ret = self.cache_data.get(key)
        if ret is not None:
            self.__used[self.__age] = key
            self.__age += 1
        return ret
