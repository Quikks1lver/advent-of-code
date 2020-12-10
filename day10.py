# 12/10/20

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/day10.txt"

def calculateVoltageDifference(adapters: List[int]) -> int:
   """
   Given a list of adapters, calculate product of 1-volt and 3-volt diffs
   """
   oneDiff: int = 0
   threeDiff: int = 0
   prev: int = 0

   for i in range(len(adapters)):
      diff: int = abs(prev - adapters[i])
      if diff == 1:
         oneDiff += 1
      elif diff == 3:
         threeDiff += 1
      else:
         continue
      prev = adapters[i]
   
   product: int = oneDiff * (threeDiff + 1) # don't forget your own adapter
   return product

def countValidArrangements(adapters: List[int], prev: int) -> int:
   """
   Using backtracking, counts valid arrangements of the adapters
   """
   # Base cases
   print(prev)
   if len(adapters) <= 0:
      return 1
   if abs(adapters[0] - prev) > 3:
      return 0
   
   valid: int = 1
   count: int = 0
   for i in range(len(adapters)):
      tempCount: int = countValidArrangements(adapters[i + 1:], adapters[i])
      if valid and tempCount:
         count += tempCount
      else:
         break
   
   return count

def main():
   adapters: List[int] = [int(s.strip()) for s in readFile(FILEPATH)]
   adapters.sort()

   # Part 1
   diff: int = calculateVoltageDifference(adapters)
   print(f"Part 1 -- Diff: {diff}")
   
   # (my attempt at) Part 2
   # numWays: int = countValidArrangements(adapters, 0)
   print(f"Part 2 -- Numways: to be continued . . . xD")

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""