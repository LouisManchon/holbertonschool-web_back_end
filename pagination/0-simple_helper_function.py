#!/usr/bin/env python3
"""
0-simple_helper_function.py
Module containing the function index_range.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    def
    """
    start = page * page_size - page_size
    end = page * page_size
    return (start, end)
