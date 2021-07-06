#!/usr/bin/env python3

from typing import List

def get_value_with_index(arr: List, index: int):
    try:
        return arr[index]
    except IndexError:
        while index > len(arr):
            index -= len(arr)
        return arr[index]

def get_index_with_value(arr: List, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i