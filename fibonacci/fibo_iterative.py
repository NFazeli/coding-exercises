def fibonacci(n):
    """
    Calculates n-th Fibonacci number iteratively

    >>> fibonacci(0)
    1
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    2
    >>> fibonacci(5)
    8
    >>> fibonacci(-1)
    Traceback (most recent call last):
      ...
    AssertionError
    """
    assert n >= 0
    if n in [0, 1]:
        return 1
    i = 2
    a, b = 1, 1
    while i <= n:
        a, b = a + b, a
        i = i + 1
    return a
