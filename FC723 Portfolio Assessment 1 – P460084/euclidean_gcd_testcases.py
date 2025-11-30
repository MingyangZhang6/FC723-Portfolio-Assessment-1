def gcd(a, b):
    """Use the Euclidean Algorithm to find the greatest common divisor（GCD）of two positive integers."""
    # store the first input number in x
    x = a
    # store the second input number in y
    y = b

    # keep looping as long as y is not zero
    while y != 0:
        # calculate the remainder when x is divided by y
        remainder = x % y
        # move the current value of y into x
        x = y
        # move the remainder into y
        y = remainder

    # when y becomes 0, x is the greatest common divisor
    return x


# test the function
if __name__ == "__main__":
    # test the gcd function with 48 and 18, expected result is 6
    print(gcd(48, 18))   # expected: 6
    # test the gcd function with 20 and 12, expected result is 4
    print(gcd(20, 12))   # expected: 4
    # test the gcd function with 7 and 5, expected result is 1
    print(gcd(7, 5))     # expected: 1