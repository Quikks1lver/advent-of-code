from Helpers.FileHelpers import read_2D_array
from functools import reduce
from typing import List, Tuple
FILEPATH = "2021/Input/day09.txt"

BLOCKING_HEIGHT = 9
CARDINAL_DIRECTIONS: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def is_inbounds(twod_array: List[List[int]], row: int, col: int) -> bool:
   return True if row >= 0 and row < len(twod_array) and col >= 0 and col < len(twod_array[0]) else False

def sum_low_point_risk_levels(heights: List[List[int]]) -> int:
   risk_levels_sum = 0

   for row in range(len(heights)):
      for col in range(len(heights[0])):
         is_lowest = True
         all_same_nums = True

         for (dx, dy) in CARDINAL_DIRECTIONS:
               new_x, new_y = row + dx, col + dy

               if is_inbounds(heights, new_x, new_y):
                  if heights[new_x][new_y] < heights[row][col]:
                     is_lowest = False
                  if heights[new_x][new_y] != heights[row][col]:
                     all_same_nums = False
         
         if is_lowest and not all_same_nums:
            risk_levels_sum += heights[row][col] + 1

   return risk_levels_sum

def lava_fill(heights: List[List[int]], is_space_flooded: List[List[bool]], row: int, col: int) -> int:
   size = 0

   for (dx, dy) in CARDINAL_DIRECTIONS:
      new_x, new_y = row + dx, col + dy

      if is_inbounds(heights, new_x, new_y) and heights[new_x][new_y] != BLOCKING_HEIGHT and not is_space_flooded[new_x][new_y]:
         is_space_flooded[new_x][new_y] = True
         size += 1 + lava_fill(heights, is_space_flooded, new_x, new_y)
   
   return size

def find_three_largest_basins(heights: List[List[int]]) -> int:
   basin_sizes: List[int] = list()
   is_space_flooded = [[False for i in range(len(heights[0]))] for j in range(len(heights))]
   
   for row in range(len(heights)):
      for col in range(len(heights[0])):
         if not is_space_flooded[row][col] and heights[row][col] != BLOCKING_HEIGHT:
            basin_sizes.append(lava_fill(heights, is_space_flooded, row, col))

   basin_sizes.sort()
   return reduce(lambda cur_product, new_val: cur_product * new_val, basin_sizes[-3:])

def main():
   heights: List[List[int]] = read_2D_array(FILEPATH, int)

   print(f"Part 1 -- {sum_low_point_risk_levels(heights)}")
   print(f"Part 2 -- {find_three_largest_basins(heights)}")

if __name__ == "__main__":
   main()