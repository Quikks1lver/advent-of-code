import math
from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.MathHelpers import count_digits_in_number
from PythonHelpers.PrintSolution import *
from typing import List
FILEPATH = "2025/Input/day06.txt"
ADD = '+'

def part1(numbers: List[List[int]], operators: List[str]) -> int:    
    total = 0
    
    for col in range(len(numbers[0])):
        should_add = operators[col] == ADD
        running_amount = 0 if should_add else 1
        
        for row in range(len(numbers)):
            if should_add:
                running_amount += numbers[row][col]
            else:
                running_amount *= numbers[row][col]
        
        total += running_amount

    return total

def part2(input: List[List[str]], numbers: List[List[int]], operators: List[str]) -> int:
    total = 0
    
    starting_index_per_column = 0
    
    for col in range(len(numbers[0])):
        operands: List[int] = []
        max_digit_number = max([count_digits_in_number(numbers[row][col]) for row in range(len(numbers))])

        for col_count in range(starting_index_per_column+max_digit_number-1, starting_index_per_column-1, -1):
            num_so_far = None

            for row in range(len(numbers)):
                val = input[row][col_count]

                if val.isspace():
                    continue
                if num_so_far is None:
                    num_so_far = int(val)
                else:
                    num_so_far *= 10
                    num_so_far += int(val)
        
            if num_so_far is not None:
                operands.append(num_so_far)

        # End-of-column processing: add to total, then for next iter,
        # skip to the max size number and skip the space in between columns.
        total += (sum(operands) if operators[col] == ADD else math.prod(operands))
        starting_index_per_column += (max_digit_number + 1)

    return total

def main() -> None:
    input: List[str] = read_lines(FILEPATH)

    numbers: List[List[int]] = []
    operators: List[str] = []

    for line in input:
        split_vals: List[str] = line.split()
        numbers_row: List[int] = []
        
        for val in split_vals:
            if split_vals[0].isdigit():
                numbers_row.append(int(val))
            else:
                operators.append(val)
        
        if len(numbers_row) > 0:
            numbers.append(numbers_row)

    PART1(part1, numbers, operators)

    # We need to ensure the input DOESN'T trim spaces for part 2.
    input2: List[str] = []
    with open(FILEPATH, "r") as fp:
        input2 = [line.rstrip('\n') for line in fp.readlines()]

    PART2(part2, input2, numbers, operators)

if __name__ == "__main__": main()
