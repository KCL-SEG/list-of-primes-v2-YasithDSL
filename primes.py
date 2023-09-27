"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math
def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("number_of_primes should be positive")
    list = []
    i = 2
    while len(list) < number_of_primes:
        check = True
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0 and j > 1:
                check = False
        if check:
            list.append(i)
        i += 1
    return list