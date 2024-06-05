#!/usr/bin/python3
"""
Coin Change Algorithm
"""


def makeChange(coins, total):
    """Calculate the fewest number needed to meet,
    needed to meet a given total amount.
    Args:
        coins ([list]): A list of coin values available.
        total ([number]): The target amount
    Return: The fewest number of coins needed to reach the total,
    or -1 if not possible.
    """
    if total <= 0:
        return 0
    # reverse the list of coins orderly
    coins.sort(reverse=True)
    index, num_coins = 0, 0
    while index < len(coins):
        if total >= coins[index]:
            total -= coins[index]
            num_coins += 1
        else:
            index += 1
    return num_coins if total == 0 else -1

