#!/usr/bin/env python3
"""
Contains Server class and index_range method.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to
    to return in a list for those particular pagination parameters.

    Args:
        page (int): the page number.
        page_size (int): the number of items per page.

    Returns:
        tuple: A tuple containing the start and end index.
    """
    start = (page - 1) * page_size
    end = page_size * page
    return (start, end)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.
        """
        #  verify that both arguments are integers greater than 0.
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        # the correct indexes to paginate the dataset correctly.
        start, end = index_range(page, page_size)

        # If the input arguments are out of range for the dataset,
        # return an empty list should be returned.
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Get a page of the dataset with hypermedia pagination.
        """
        # get the page dat from get_page
        data = self.get_page(page, page_size)

        # Total pages
        total_pages = math.ceil(len(self.dataset()) / page_size)

        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
