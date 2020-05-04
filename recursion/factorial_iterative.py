def factorial(n):
    """
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
    i = 2
    a = 1
    while i <= n:
        a = a * i
        i += 1
    return a



    return a