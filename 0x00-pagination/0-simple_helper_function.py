#!/usr/bin/env python3
"""
Contains index_range method
"""


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
