#!/usr/bin/python3
"""Finding the minimum number of operations"""


def minOperations(n):
    """Finding minimum operations of copy all and paste
    required to product the n H characters"""
    if n <= 1:
        return 0
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1
    return operations
