#!/usr/bin/env python3
""" Python Script on Pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Helper function """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
