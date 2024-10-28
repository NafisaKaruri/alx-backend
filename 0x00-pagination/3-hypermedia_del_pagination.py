#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get a page of the dataset based on index and page size.
        """
        # validate index
        assert index is not None and 0 <= index < len(self.__indexed_dataset)

        data = []  # indexed data
        current_index = index  # current index
        items_fetched = 0

        # Fetch the required data
        while items_fetched < page_size:
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                items_fetched += 1
            current_index += 1

        # Prepare the result
        if current_index < len(self.__indexed_dataset):
            next_index = current_index
        else:
            None

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
