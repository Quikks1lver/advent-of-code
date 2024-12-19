from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2022/Input/day01.txt"

def calculate_calories(input: List[str]) -> List[int]:
    calories: List[int] = list()
    running_total = 0
    for val in input:
        if val == '\n':
            calories.append(running_total)
            running_total = 0
        else:
            running_total += int(val)
    return calories

def main():
   input_lines: List[int] = read_lines(FILEPATH)
   
   calories = calculate_calories(input_lines)
   print(f"Part 1 -- {max(calories)}")
   
   calories.sort()
   print(f"Part 2 -- {sum(calories[-3:])}")

if __name__ == "__main__": main()