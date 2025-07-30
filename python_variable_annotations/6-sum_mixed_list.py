#!/usr/bin/env python3
"""
Funtion which takes a list mxd_lst of integers
and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    which takes a list mxd_lst of integers
    and floats and returns their sum as a float
    """
    result: float = 0.00
    number: float
    for number in mxd_lst:
        result += number
    return result
