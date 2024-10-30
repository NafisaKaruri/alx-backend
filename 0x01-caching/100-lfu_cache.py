#!/usr/bin/env python3
"""
Contains LFUCache class that inherits from BaseCaching.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class.
    """
    def __init__(self):
        """
        Initialize.
        """
        super().__init__()
        self.cache_data = {}
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """
        Assign to self.cache_dat the item value for the key key.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lfu_key = min(
                    self.frequency,
                    key=lambda k: (self.frequency[k], self.order.index(k))
                )
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.order.remove(lfu_key)
                print(f'DISCARD: {lfu_key}')
            self.frequency[key] = 1
        self.order.append(key)

    def get(self, key):
        """
        Return the value in self.cache_data linked to key.
        """
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
