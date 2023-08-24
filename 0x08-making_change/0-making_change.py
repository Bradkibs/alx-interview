#!/usr/bin/python3
""" An implementation of finding the fewest number of change
for a given amount"""

from collections import deque


def makeChange(coins, total):
    """given coins as a list and total as a number
    required to figure out how many coins can get that total using
    the fewest number of coins"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    dequed_coins = deque(coins)
    count = 0
    while True:
        if len(dequed_coins) != 0:
            if total == 0:
                break
            num_of_coins = total // dequed_coins[0]
            count += num_of_coins
            total -= (num_of_coins * dequed_coins[0])
            dequed_coins.popleft()
        else:
            if total != 0:
                return -1
            break
    return count
