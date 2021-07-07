#!/usr/bin/env python3

from typing import List

def get_value_with_index(arr: List, index: int):
    """This function returns your target value in your list without IndexError!
    If your index is out of range, it will decrease the length of the list and
    try to return your value again.
    
    for example:
    >>> get_value_with_index([1,2,3], 6)
    >>> 1
    
    beacuse:
    index:  values:
        0       1
        1       2
        2       3
        3       1
        4       2
        5       3
        6       1
    """

    try:
        return arr[index]
    except IndexError:
        while index >= len(arr):
            index -= len(arr)
        return arr[index]

def get_index_with_value(arr: List, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i

def get_indexs_with_values(arr: List, values: List) -> list:
    res = []
    for i in range(len(arr)):
        for j in values:
            if arr[i] == j and i not in res:
                res.append(i)
    return res

def get_indexs_with_value(arr: List, value):
    res = []
    for i in range(len(arr)):
        if arr[i] == value:
            res.append(i)
    return res
    