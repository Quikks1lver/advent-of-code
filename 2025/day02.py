from collections import defaultdict
from math import ceil
from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import DefaultDict, List, Set, Tuple
FILEPATH = "2025/Input/day02.txt"

def count_digits_in_number(x: int) -> int:
    if x == 0:
        return 1
    
    num_digits = 0

    while True:
        if x == 0:
            return num_digits
        x //= 10
        num_digits += 1

def get_unique_digit_counts(x: int) -> DefaultDict[int, int]:
    dict: DefaultDict[int, int] = defaultdict(int)

    if x == 0:
        dict[0] += 1
        return dict

    while True:
        if x == 0:
            return dict
        dict[x % 10] += 1
        x //= 10

def is_num_consisting_of_repeated_sequence(x: int) -> bool:
    str_x = str(x)
    num_digits = len(str_x)

    for chunk_len in range(1, num_digits // 2 + 1):
        match_expr = ""
        success = True
        
        for start_index in range(0, num_digits, chunk_len):
            str_chunk = str_x[start_index : start_index + chunk_len]
            if match_expr == "":
                match_expr = str_chunk
            else:
                if match_expr != str_chunk:
                    success = False
                    break

        if success:
            return True

    return False

def part1(input: List[Tuple[int, int]]) -> int:
    invalid_sum = 0

    for chunk in input:
        for i in range(chunk[0], chunk[1] + 1):
            num_digits = count_digits_in_number(i)
            
            # If number of digits is odd, can't possibly be a number followed by itself.
            if num_digits % 2 == 1:
                continue
            
            halfway_pt = num_digits // 2
            first_half, second_half = 0, 0
            number_to_use = i

            for digit in range(num_digits, 0, -1):
                if digit <= halfway_pt:
                    exponent = halfway_pt - digit
                    first_half += (number_to_use % 10) * (10 ** exponent)
                else:
                    exponent = num_digits - digit
                    second_half += (number_to_use % 10) * (10 ** exponent)
                number_to_use //= 10
            
            if first_half == second_half:
                invalid_sum += i

    return invalid_sum

def part2(input: List[Tuple[int, int]]) -> int:
    invalid_sum = 0

    for chunk in input:
        for i in range(chunk[0], chunk[1] + 1, 1):
            if is_num_consisting_of_repeated_sequence(i):
                invalid_sum += i
    
    return invalid_sum

def main() -> None:
    input: List[Tuple[int, int]] = [
        (int(mini_str[0]), int(mini_str[1]))
        for line in read_lines(FILEPATH)
        for l in line.split(',')
        for mini_str in [l.split('-')]
    ]

    PART1(part1, input)
    PART2(part2, input)

if __name__ == "__main__": main()