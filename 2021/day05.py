from Helpers.FileHelpers import read_lines
from functools import reduce
from typing import List, Dict, Tuple
FILEPATH = "2021/Input/day05.txt"

def create_segment_map(line_segments: List[List[Tuple[int, int]]], delta_0: bool) -> Dict[Tuple[int, int], int]:
   segment_map: Dict[Tuple[int, int], int] = dict()

   for segment in line_segments:
      x1, y1 = segment[0]
      x2, y2 = segment[1]

      delta_x = 1 if x1 < x2 else 0 if x1 == x2 else -1
      delta_y = 1 if y1 < y2 else 0 if y1 == y2 else -1

      # check for horizontal/vertical lines
      if not delta_0:
         pass
      elif not (delta_0 and (delta_x == 0 or delta_y == 0)):
         continue

      coord = (x1, y1)
      while coord != (x2 + delta_x, y2 + delta_y):
         if coord in segment_map.keys():
            segment_map[coord] += 1
         else:
            segment_map[coord] = 1

         coord = (coord[0] + delta_x, coord[1] + delta_y)

   return segment_map

def get_num_overlapping_points(segment_map: Dict[Tuple[int, int], int]) -> int:
   count = 0
   for val in segment_map.values():
      if val > 1:
         count += 1
   return count

def main():
   line_segments = [line.strip().split(" -> ") for line in read_lines(FILEPATH)]
   line_segments: List[List[Tuple[int, int]]] = [[tuple(int(x) for x in segment[0].split(",")), tuple(int(x) for x in segment[1].split(","))] for segment in line_segments]

   print(f"Part 1 -- {get_num_overlapping_points(create_segment_map(line_segments, True))}")
   print(f"Part 2 -- {get_num_overlapping_points(create_segment_map(line_segments, False))}")

if __name__ == "__main__":
   main()