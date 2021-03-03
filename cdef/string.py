#!/bin/env python3

"""
This Module Like string library in the C Language!
this Module Have Functions like <string.h> Functions :D
"""

def strchr(text: str, char: str) -> str:
    """
    this function geting text and one char and
    return after all char after your char if your char
    finde in the text.

    >>> import String
    >>> String.strchr("emad is here :D" , ":")
    ':D'
    >>> String.strchr("emad","maaaa")
    'mad'
    """
    def creat_char(text: str) -> str:
        return text[0]
    def cuter(text: str, index: int) -> str:
        result = ""
        for i in range(index, len(text)):
            result += text[i]
        return result

    if len(char) > 1:
        char = creat_char(char)
    find_index = -1
    for i in range(len(text)):
        if text[i] == char:
            find_index = i

    if find_index != -1:
        return cuter(text, find_index)

#TODO; wh have a Bug here :(
def strcspn(text_one: str, text_tow: str) -> int:
    def valid(char: str):
        if not(char in "!@#$%^&*()_-+=<>,./\\[]{}'\";:`~"):
            return True
        else:
            return False

    result = 0
    for i in text_one:
        find = False
        for j in text_tow:
            if valid(i) and i == j:
                find = True
                break
        if not find:
            result += 1
    return result

#TODO: wh have a bug here i need time for fix it
def strstr(text: str, target: str) -> str:
    def cuter(text: str, start_point: int) -> str:
        result = ""
        for i in range(start_point, len(text)):
            if text[i] == " ":
                break
            result += text[i]
        return result

    find_index = -1
    for i in range(0, len(text), len(target)):
        if text[i:i+(len(target)-1)] == target:
            if i + 1 < len(text) - 1:
                find_index = i + 1

    if find_index != -1:
        return cuter(text, find_index)
