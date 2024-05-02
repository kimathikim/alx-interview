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

    coins.sort(reverse=True)

    index, num_coins = (0, 0)
    copy_total = total
    len_coins = len(coins)

    while (index < len_coins and copy_total > 0):
        if (copy_total - coins[index]) >= 0:
            copy_total -= coins[index]
            num_coins += 1
        else:
            index += 1

    check = copy_total > 0 and num_coins > 0
    return -1 if check or num_coins == 0 else num_coins
