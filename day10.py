# 12/10/20

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/day10.txt"

def calculateVoltageDifference(adapters: List[int]) -> int:
   """
   Given a list of adapters, calculate product of 1-volt and 3-volt diffs
   """
   oneDiff: int = 0
   threeDiff: int = 1 # your phone adapter's diff
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
   
   return oneDiff * threeDiff

def countValidArrangements(adapters: List[int]) -> int:
   """
   Counts valid arrangements of the adapters (sorted list)
   """
   paths: List[int] = [0] * (adapters[-1] + 1)
   paths[0] = 1

   for index in range(1, adapters[-1] + 1):
      for i in range(1, 4):
         if index - i in adapters:
            paths[index] += paths[index - i]
   
   return paths[-1]

def main():
   adapters: List[int] = [int(s.strip()) for s in readFile(FILEPATH)]
   adapters.append(0) # outlet
   adapters.sort()

   # Part 1
   diff: int = calculateVoltageDifference(adapters)
   print(f"Part 1 -- Diff: {diff}")
   
   # Part 2
   # I was stumped on this problem, so I looked up a video to help me understand dynamic programming,
   # something I have never learned or tackled before. This video is what helped me solve the problem:
   # https://www.youtube.com/watch?v=eeYanhLamjg.
   numWays: int = countValidArrangements(adapters)
   print(f"Part 2 -- Numways: {numWays}")

if __name__ == "__main__":
   main()

"""
--- Day 10: Adapter Array ---
--- Part One ---
If you use every adapter in your bag at once, what is the distribution of joltage differences between
the charging outlet, the adapters, and your device?
Find a chain that uses all of your adapters to connect the charging outlet to your device's built-in
adapter and count the joltage differences between the charging outlet, the adapters, and your device.
What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
--- Part Two ---
What is the total number of distinct ways you can arrange the adapters to connect the charging outlet
to your device?
"""