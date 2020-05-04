def factorial(n):
    """
    calculate factorial of n recursive
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(4)
    24
    """

    assert n >= 0
    if n in [0, 1]:
        return 1
    return n*factorial(n-1)
