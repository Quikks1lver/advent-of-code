from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2025/Input/day01.txt"

def part1(input: List[Tuple[str, int]]) -> int:
   curr_position = 50
   num_zeros = 0

   for item in input:
      modded_value = item[1] % 100
      
      if item[0] == 'R':
         curr_position += modded_value
      else: # 'L'
         temp_pos = curr_position - modded_value
         if temp_pos < 0:
            temp_pos += 100
         curr_position = temp_pos

      curr_position %= 100

      if curr_position == 0:
         num_zeros += 1

   return num_zeros

def part2(input: List[Tuple[str, int]]) -> int:
   curr_position = 50
   num_zeros = 0
   num_turnover_zeros = 0

   for item in input:
      modded_value = item[1] % 100
      num_turnover_zeros += item[1] // 100
      
      if item[0] == 'R':
         curr_position += modded_value
         # If our temporary position went greater than 100, this means we've
         # went past zero clockwise.
         if curr_position > 100:
            num_turnover_zeros += 1
      else: # 'L'
         temp_pos = curr_position - modded_value
         if temp_pos < 0:
            # If our temporary position is negative, this means we've went
            # past zero counterclockwise. If we weren't already at 0, don't
            # double count, then increase the counter.
            if curr_position != 0:
               num_turnover_zeros += 1
            temp_pos += 100
         curr_position = temp_pos

      curr_position %= 100

      if curr_position == 0:
         num_zeros += 1

   return num_zeros + num_turnover_zeros

def main() -> None:
   input: List[Tuple[str, int]] = [(line[:1], int(line[1:].strip())) for line in read_lines(FILEPATH)]
   
   PART1(part1, input)
   PART2(part2, input)

if __name__ == "__main__": main()