def count_digits_in_number(x: int) -> int:
    """
    Counts number of digits in the specified base 10 number.
    """
    if x == 0:
        return 1
    
    num_digits = 0

    while True:
        if x == 0:
            return num_digits
        x //= 10
        num_digits += 1