#!/usr/bin/env python3
"""
Contains LRUCache class that inherits from BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class.
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
        if key in self.cache_data:
            self.order.remove(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f'DISCARD: {lru_key}')
        self.order.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]