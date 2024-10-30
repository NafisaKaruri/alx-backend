#!/usr/bin/env python3
"""
Contains FIFOCache class that inherits from BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign to self.cache_dat the item value for the key key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            self.order.append(key)  # Keep track of the order of keys
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f'DISCARD: {oldest_key}')

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
