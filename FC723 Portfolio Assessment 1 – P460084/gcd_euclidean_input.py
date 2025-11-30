def gcd(a, b):
    """Use the Euclidean Algorithm to find the GCD of two positive integers."""
    x = a                          # put the first number into x
    y = b                          # put the second number into y

    while y != 0:                  # keep looping while y is not zero
        remainder = x % y          # remainder is x divided by y (the leftover)
        x = y                      # move y into x for the next step
        y = remainder              # move the remainder into y

    return x                       # when y becomes zero, x is the greatest common divisor


def get_positive_int(prompt):
    """Ask the user for a positive integer and repeat until the input is valid."""
    while True:                                # repeat until we get a valid input
        user_input = input(prompt)             # ask the user to type something

        try:
            value = int(user_input)            # try to convert the input into an integer
        except ValueError:                     # this runs if the input is not an integer
            print("Please enter a whole number (integer).")
            continue                           # go back and ask again

        if value <= 0:                         # check if the number is zero or negative
            print("Please enter a positive integer greater than zero.")
            continue                           # number is not valid, ask again

        return value                           # number is OK, send it back to the caller


if __name__ == "__main__":                     # only run this block when the file is run directly
    print("Euclidean Algorithm - GCD of two positive integers")  # show a simple title
    print()                                    # print an empty line

    a = get_positive_int("Enter the first positive integer: ")   # get the first number from the user
    b = get_positive_int("Enter the second positive integer: ")  # get the second number from the user

    result = gcd(a, b)                         # call gcd with a and b and save the result

    print()                                    # print another empty line
    print(f"The greatest common divisor of {a} and {b} is {result}.")  # show the final answer