def euclidean(a: int, b: int) -> int:
    """
        The Euclid's algorithm utilizes the concept of greatest common divisor to calculate the power of two ints.

        For example if we wanted to calculate 7 ** 121 we could also do it like this
        7 ** 121 = (7 ** 60) * (7 ** 60) * 7
        Thanks to this logic we make fewer operations and the calculations are faster.
    """
    # Base case
    if b == 0:
        return 1

    # Calculate `a` to the power of `b // 2`
    x = euclidean(a, b // 2)

    # Utilize result of above calculations
    y = x * x
    if b % 2 == 1:
        y = y * a

    return y


if __name__ == '__main__':
    assert euclidean(2, 5) == 32
    assert euclidean(5, 7) == 78125
    assert euclidean(100, 0) == 1
