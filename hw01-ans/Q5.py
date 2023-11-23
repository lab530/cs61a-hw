def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    step = 1
    while True:
        print(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        step += 1
    return step