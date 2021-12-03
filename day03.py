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

def calculate_filtered_value(diagnostics: List[str], most_common: bool) -> str:
   val_set = set([i for i in range(0, len(diagnostics))])
   pos_check = "1" if most_common else "0"
   neg_check = "0" if most_common else "1"
   index = 0

   while len(val_set) != 1:
      ones_zeros_diff = 0
      
      # calculate difference between ones and zeros based on which strings are left at this iteration
      for count, string in enumerate(diagnostics):
         if count in val_set:
            ones_zeros_diff += (1 if string[index] == "1" else -1)

      # filter out strings based on the diff: most v. least common majority of 0s/1s
      for count, string in enumerate(diagnostics):
         if count in val_set:
            if (ones_zeros_diff >= 0 and string[index] == pos_check) or (ones_zeros_diff < 0 and string[index] == neg_check):
               pass
            else:
               val_set.remove(count)

      index += 1

   return diagnostics[val_set.pop()]

def calculate_life_support_rating(diagnostics: List[str]) -> int:
   ox_string = calculate_filtered_value(diagnostics, True)
   co2_string = calculate_filtered_value(diagnostics, False)
   return int(ox_string, 2) * int(co2_string, 2)

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {calculate_power_consumption(input_lines)}")
   print(f"Part 2 -- {calculate_life_support_rating(input_lines)}")

if __name__ == "__main__":
   main()