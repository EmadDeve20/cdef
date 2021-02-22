#!/bin/env python3

class String:
    """this is class about string like <string.h> library in the C"""
    def strstr(text: str, target: str):
        result = ""
        find_index = 0
        for i in range(len(text)):
            if text[i:i + len(target)] == target:
                find_index = i
                break
        for i in range(find_index, len(text)):
            if text[i] != " ":
                result += text[i]
            else:
                break
        return result
