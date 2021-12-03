from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "Input/day03.txt"

def calculate_power_consumption(diagnostics: List[str]) -> int:
   sums: List[int] = [0] * len(diagnostics[0])

   for string in diagnostics:
      for count, val in enumerate(string):
         sums[int(count)] += (1 if val == "1" else -1)

   gamma, epsilon = 0, 0
   for count, val in enumerate(sums):
      power_of_two = (2 ** (len(sums) - count - 1))
      
      # 1s dominate
      if val > 0:
         gamma += power_of_two

      # 0s dominate
      else:
         epsilon += power_of_two
   
   return gamma * epsilon

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {calculate_power_consumption(input_lines)}")
   # print(f"Part 2 -- {}")

if __name__ == "__main__":
   main()