"""Determining if a given data set represents a valid UTF-8 encoding"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """A function determines if a given data set represents a
    a valid UTF-8 encoding"""
    for item in data:
        if (item > 255):
            return False
    return True
