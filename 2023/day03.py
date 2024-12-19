from Helpers.FileHelpers import read_2D_array
from typing import Union, List, Dict, Tuple
FILEPATH = "2023/Input/day03.txt"
from collections import defaultdict

inBounds = lambda row, col, dimensions: row >= 0 and row < dimensions[0] and col >= 0 and col < dimensions[1]

def isAdjacentToSymbol(input: List[List[str]], row: int, col: int, dimensions: Tuple[int, int]) -> Union[None, Tuple[int, int]]:
   for i in range(-1, 2, 1):
      for j in range(-1, 2, 1):
         newRow, newCol = row + i, col + j

         if not inBounds(newRow, newCol, dimensions):
            continue
         
         val = input[newRow][newCol]
         if val != '.' and not val.isdigit():
            return newRow, newCol
   return None

def part1(input: List[List[str]], dimensions: Tuple[int, int]) -> int:
   total = 0
   numberStr = ""
   validPartNum = False

   for row in range(dimensions[0]):
      for col in range(dimensions[1]):
         val = input[row][col]

         if not val.isdigit():
            if numberStr != "" and validPartNum:
               total += int(numberStr)
            numberStr = ""
            validPartNum = False
            continue

         numberStr += val

         if isAdjacentToSymbol(input, row, col, dimensions):
            validPartNum = True

   return total

def part2(input: List[List[str]], dimensions: Tuple[int, int]) -> int:
   gearToNumMap: Dict[Tuple[int, int], List[int]] = defaultdict(list)
   locationOfGear: Tuple[int, int] = None
   numberStr = ""

   for row in range(dimensions[0]):
      for col in range(dimensions[1]):
         val = input[row][col]

         if not val.isdigit():
            if numberStr != "" and locationOfGear is not None:
               gearToNumMap[locationOfGear].append(int(numberStr))
            
            numberStr = ""
            locationOfGear = None
            continue

         numberStr += val

         if locationOfGear is None:
            locationOfGear = isAdjacentToSymbol(input, row, col, dimensions)

   total = 0

   for val in gearToNumMap.values():
      if len(val) == 2:
         total += (val[0] * val[1])

   return total

def main():
   input: List[List[str]] = read_2D_array(FILEPATH, str)
   dimensions: Tuple[int, int] = len(input), len(input[0])
   
   print(f"Part 1 -- {part1(input, dimensions)}")
   print(f"Part 2 -- {part2(input, dimensions)}")


if __name__ == "__main__": main()