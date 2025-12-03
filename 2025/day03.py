from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2025/Input/day03.txt"

# Returns [index, val]. Checks bounds inclusively.
def get_largest_left_most_num(line: List[int], starting_left_index: int, starting_right_index: int) -> Tuple[int, int]:
    # Sanity checks for bounds.
    assert starting_left_index >= 0
    assert starting_right_index < len(line)
    assert starting_left_index <= starting_right_index
    
    largest_val = line[starting_right_index]
    largest_val_index = starting_right_index

    for i in range(starting_right_index - 1, starting_left_index - 1, -1):
        curr_val = line[i]
        if curr_val >= largest_val:
            largest_val = curr_val
            largest_val_index = i
    
    return (largest_val_index, largest_val)

def solve(input: List[List[int]], num_digit_number: int) -> int:
    retval = 0
    arr_length = len(input[0])

    for line in input:
        curr_product = 0

        # For very first run through, left bound index is left end of array: we want to check all elements.
        # Right index means we start with array length - 12, so that way if largest left most number is the
        # 12th last digit, we can still complete the 12 digit number.
        left_bound_index = 0
        right_bound_index = arr_length - num_digit_number

        for _ in range(num_digit_number):
            largest_val_index, largest_val = get_largest_left_most_num(line, left_bound_index, right_bound_index)

            # Always replace left bound index with new sliding window.
            left_bound_index = largest_val_index + 1
            
            # Make sure we always have enough numbers left over to complete a 12 digit number.
            # Hence, adjust sliding window one notch over.
            right_bound_index += 1

            # Horner's rule
            curr_product *= 10
            curr_product += largest_val

        retval += curr_product

    return retval

def main() -> None:
    input: List[List[int]] = [[int(ch) for ch in line] for line in read_lines(FILEPATH)]
    
    PART1(solve, input, 2)
    PART2(solve, input, 12)

if __name__ == "__main__": main()
