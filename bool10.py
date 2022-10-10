def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    from math import sqrt
    return sqrt(a) % 1 == 0

print(main(64))