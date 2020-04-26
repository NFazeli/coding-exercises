def fibonacci(n):
    """
    Calculates n-th Fibonacci number recursively

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
    return fibonacci(n - 1) + fibonacci(n - 2)
