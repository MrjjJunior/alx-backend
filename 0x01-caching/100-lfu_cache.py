#!/usr/bin/env python3
"""LFU Caching"""
from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFU Cache system inheriting from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.frequency = defaultdict(int)  # Track access frequency of each key
        self.usage_order = []  # Track the order of usage to handle LRU

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu = [k for k, v in self.frequency.items() if v == min_freq]

                if len(lfu) > 1:
                    for k in self.usage_order:
                        if k in lfu:
                            discard_key = k
                            break
                else:
                    discard_key = lfu[0]

                print(f"DISCARD: {discard_key}")
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                self.usage_order.remove(discard_key)

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.usage_order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
