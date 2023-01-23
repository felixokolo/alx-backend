#!/usr/bin/env python3

"""
Pagination
"""

from typing import Tuple

def index_range(page: int,
                page_size: int) -> Tuple[int, int]:
        """
        Calculation of start and end index of page
        """
        start_idx : int = (page - 1) * page_size
        end_idx : int = page * page_size
        return (start_idx, end_idx)