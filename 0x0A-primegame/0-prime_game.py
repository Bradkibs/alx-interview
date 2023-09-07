#!/usr/bin/python3
"""Algorithm for the prime game"""

import math


def isWinner(x, nums):
    """Determines between maria and Ben who wins the game"""
    score = {"Maria": 0, "Ben": 0}

    def isPrime(n):
        """Does a prime check on a given number"""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    for item in nums:
        primes = [i for i in range(2, item + 1) if isPrime(i)]
        if len(primes) % 2 == 0:
            score["Ben"] += 1
        else:
            score["Maria"] += 1

    if (score["Maria"] < score["Ben"]):
        return("Ben")
    return("Maria")
