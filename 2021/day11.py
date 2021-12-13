from Helpers.FileHelpers import read_lines, read_2D_array
from sys import maxsize
from typing import List, Set, Tuple
FILEPATH = "2021/Input/day11.txt"

FLASH_THRESHOLD = 9

def flash_adjacent_cells(octopi: List[List[int]], row: int, col: int) -> None:
   delta = range(-1, 2, 1)
   row_bound, col_bound = len(octopi) - 1, len(octopi[0]) - 1
   
   for x in delta:
      for y in delta:
         new_x, new_y = row + x, col + y
         if new_x >= 0 and new_x <= row_bound and new_y >= 0 and new_y <= col_bound:
            octopi[new_x][new_y] += 1

def count_flashes(octopi: List[List[int]], num_steps: int, is_searching_for_synchronous_flash: bool) -> int:
   num_flashes = 0
   octopi_copy = octopi.copy()

   for _ in range(num_steps):
      octopi_copy = [[col_val + 1 for col_val in row] for row in octopi_copy]
      flashed_set: Set[Tuple[int, int]] = set()
      keep_going = True

      while keep_going:
         keep_going = False        

         for row in range(len(octopi_copy)):
            for col in range(len(octopi_copy[0])):
               if (row, col) not in flashed_set and octopi_copy[row][col] > FLASH_THRESHOLD:
                  num_flashes += 1
                  flash_adjacent_cells(octopi_copy, row, col)
                  octopi_copy[row][col] = 0
                  flashed_set.add((row, col))
                  keep_going = True

         if is_searching_for_synchronous_flash and len(flashed_set) == len(octopi_copy) * len(octopi_copy[0]):
            return _ + 1

         for row, col in flashed_set:
            octopi_copy[row][col] = 0

   return num_flashes

def main():
   octopi: List[List[int]] = read_2D_array(FILEPATH, int)

   print(f"Part 1 -- {count_flashes(octopi, 100, False)}")
   print(f"Part 2 -- {count_flashes(octopi, maxsize, True)}")

if __name__ == "__main__":
   main()