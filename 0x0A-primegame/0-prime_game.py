#!/usr/bin/python3
"""Algorithm for the prime game"""


def isWinner(x, nums):
    """Determines between maria and Ben who wins the game"""
    score = {"Maria": 0, "Ben": 0}

    def isPrime(n):
        """Does a prime check on a given number"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for item in nums:
        available_numbers = list(range(2, item + 1))

        maria_turn = True

        while available_numbers:
            valid_choices = [num for num in available_numbers if isPrime(num)]
            if not valid_choices:
                break

            chosen_prime = max(valid_choices)

            available_numbers = [num for num in available_numbers
                                 if num % chosen_prime != 0]

            maria_turn = not maria_turn

        if maria_turn:
            score["Ben"] += 1
        else:
            score["Maria"] += 1

    if score["Maria"] < score["Ben"]:
        return "Ben"
    elif score["Maria"] == score["Ben"]:
        return None
    else:
        return "Maria"
