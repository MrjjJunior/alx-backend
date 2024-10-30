#!/usr/bin/env python3
""" Python Module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic Cache Class """

    def put(self, key, item):
        """ Put item in cache """

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get item from cache """
        if key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)
