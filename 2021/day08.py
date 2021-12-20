from functools import reduce
from Helpers.FileHelpers import read_lines
from typing import List, Tuple
FILEPATH = "2021/Input/day08.txt"

SEV_SEG_EZ_NUM_LENGTHS = {2, 3, 4, 7}

def parse_input(input_lines: List[str]) -> Tuple[List[List[str]], List[List[str]]]:
   signal_patterns: List[List[str]] = []
   output_values: List[List[str]] = []

   for _ in input_lines:
      s = _.split("|")
      signal_patterns.append(s[0].split())
      output_values.append(s[1].split())

   return signal_patterns, output_values

def count_easy_digits(output_values: List[List[str]]) -> int:
   count = 0
   for row in output_values:
       for string in row:
          if len(string) in SEV_SEG_EZ_NUM_LENGTHS:
             count += 1
   return count

def main():
   signal_patterns, output_values = parse_input([line.strip() for line in read_lines(FILEPATH)])

   print(f"Part 1 -- {count_easy_digits(output_values)}")
   # print(f"Part 2 -- {}")

if __name__ == "__main__":
   main()