from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2021/Input/day06.txt"

FISH_RESET_TIMER = 6
MAX_FISH_TIMER = 8

def create_deduped_fish_frequencies_list(raw_frequencies: List[int]) -> List[int]:
   deduped_fish_frequencies: List[int] = [0 for i in range(MAX_FISH_TIMER + 1)]

   for freq in raw_frequencies:
      deduped_fish_frequencies[freq] += 1
   
   return deduped_fish_frequencies

def simulate_fish(fish_frequencies: List[int], num_days: int) -> int:
   for _ in range(num_days):
      new_frequencies = [0 for i in range(MAX_FISH_TIMER + 1)]

      for index, val in enumerate(fish_frequencies):   
         if index == 0:
            new_frequencies[FISH_RESET_TIMER] = val
            new_frequencies[MAX_FISH_TIMER] = val
         else:
            new_frequencies[index - 1] += val

      fish_frequencies = new_frequencies

   return sum(fish_frequencies)

def main():
   raw_fish_frequencies: List[int] = [[int(x) for x in line.strip().split(",")] for line in read_lines(FILEPATH)][0]
   deduped_frequencies = create_deduped_fish_frequencies_list(raw_fish_frequencies)

   print(f"Part 1 -- {simulate_fish(deduped_frequencies, 80)}")
   print(f"Part 2 -- {simulate_fish(deduped_frequencies, 256)}")

if __name__ == "__main__":
   main()