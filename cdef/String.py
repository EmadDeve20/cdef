#!/bin/env python3

#TODO: wh have a bug here i need time for fix it
def strstr(text: str, target: str):
    result = ""
    find_index = 0
    is_find = False
    for i in range(len(text)):
        if (i+len(target) < len(text)) and (text[i + len(target)-1] == target):
            find_index = i+1
            is_find = True
            break
    if is_find:
        for i in range(find_index, len(text)):
            if text[i] != " ":
                result += text[i]
            else:
                break
    return result
