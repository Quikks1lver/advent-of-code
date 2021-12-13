from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2021/Input/day07.txt"

def calculate_fuel_consumption(dx: int, is_constant_rate: bool) -> int:
   return dx if is_constant_rate else (dx) * (dx + 1) / 2

def calculate_min_fuel_consumption(positions: List[int], is_constant_rate: bool) -> int:
   distance_map = {x : 0 for x in range(min(positions), max(positions) + 1)}
   
   for dist in distance_map.keys():
      for pos in positions:
         distance_map[dist] += calculate_fuel_consumption(abs(pos - dist), is_constant_rate)

   return min(distance_map.values())

def main():
   positions: List[int] = [int(x) for x in read_lines(FILEPATH)[0].split(",")]

   print(f"Part 1 -- {calculate_min_fuel_consumption(positions, True)}")
   print(f"Part 2 -- {calculate_min_fuel_consumption(positions, False)}")

if __name__ == "__main__":
   main()