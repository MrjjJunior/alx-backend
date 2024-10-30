#!/usr/bin/env python3
""" Python Script """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOcache class """

    def __init__(self):
        super().__init__()
        self.insert_order = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.insert_order.remove(key)

            self.cache_data[key] = item
            self.insert_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.insert_order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Gets an item by key """
        return self.cache_data.get(key, None)
