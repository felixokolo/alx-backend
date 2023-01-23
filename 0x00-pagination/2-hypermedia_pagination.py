#!/usr/bin/env python3

"""
Pagination
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int,
                page_size: int) -> Tuple[int, int]:
    """
    Calculation of start and end index of page
    """
    start_idx: int = (page - 1) * page_size
    end_idx: int = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Gets a page
        """
        assert(type(page) is int and type(page_size) is int)
        assert(page > 0 and page_size > 0)
        dataset = self.dataset()
        start_idx, end_idx = index_range(page, page_size)
        if len(dataset) < start_idx:
            return []
        if end_idx > len(dataset):
            end_idx = None
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get page details
        """

        page_list = self.get_page(page, page_size)
        next_page = self.get_page(page + 1, page_size)
        prev_page = None
        try:
            prev_page = self.get_page(page - 1, page_size)
        except(AssertionError):
            pass
        total_pages = len(self.dataset()) // page_size
        if len(self.dataset()) % page_size > 0:
            total_pages += 1
        ret = {'page_size': len(page_list),
               'page': page,
               'data': page_list,
               'next_page': None if len(next_page) == 0 else page + 1,
               'prev_page': page - 1 if prev_page is not None else None,
               'total_pages': total_pages}
        return ret
