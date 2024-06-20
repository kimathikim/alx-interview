#!/usr/bin/python3

'''This module contains a function that determines
the winner of a game based on prime numbers.'''


def isWinner(x, nums):
    def sieve(n):
        """ Return a list of primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
                p += 1
        primes = [p for p in range(2, n + 1) if is_prime[p]]
        return primes

    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0

    for n in nums:
        primes_count = len([p for p in primes if p <= n])
        if primes_count % 2 == 1:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
