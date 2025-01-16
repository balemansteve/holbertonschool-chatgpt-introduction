#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    Calculate the factorial of a non-negative integer recursively.
    
    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.
    
    Returns:
    int: The factorial of the given number. If n is 0, returns 1 (base case).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
