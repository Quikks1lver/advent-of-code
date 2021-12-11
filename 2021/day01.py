from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2021/Input/day01.txt"

def count_increasing_nums(lines: List[int]) -> int:
   count = 0

   for i in range(len(lines) - 1):
      if lines[i + 1] > lines[i]:
         count += 1 

   return count

def count_triples(lines: List[int]) -> int:
   count = 0

   for i in range(1, len(lines) - 2):
      if lines[i - 1] + lines[i] + lines[i + 1] < lines[i] + lines[i + 1] + lines[i + 2]:
         count += 1
   
   return count

def main():
   input_nums = [int(line.strip()) for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {count_increasing_nums(input_nums)}")
   print(f"Part 2 -- {count_triples(input_nums)}")

if __name__ == "__main__":
   main()