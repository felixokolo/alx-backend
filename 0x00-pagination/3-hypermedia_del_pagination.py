#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple


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
        """
        Get hyper index
        """
        dataset = self.indexed_dataset()
        assert(index <= len(dataset) // page_size)
        idxz = list(dataset.keys())
        sorted(idxz)
        start_idx, end_idx = index, index + page_size
        if end_idx > len(idxz):
            end_idx = None
        idxs = idxz[start_idx:end_idx]
        page_list = [dataset.get(i) for i in idxs]
        ret = {'index': start_idx,
               'next_index': idxz[end_idx] if end_idx is not None else None,
               'page_size': len(page_list),
               'data': page_list}
        return ret
