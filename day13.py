# 12/13/20

from Helpers.FileHelper import readFile
from typing import List, Tuple
FILEPATH: str = "Input/day13.txt"

def findClosestMultipleAboveThreshold(num: int, threshold: int) -> int:
   """
   Returns the number's closest multiple above the threshold
   """
   while True:
      if threshold % num == 0:
         return threshold
      else:
         threshold += 1

def calculateWeightedWaitTime(yourTime: int, buses: List[int]) -> int:
   """
   Finds bus closest to wait time and computes ID of the bus * wait time
   """
   targetBus: int = 0
   waitTime: int = 0
   minDiff: int = 0
   first: bool = True

   for bus in buses:
      diff: int = findClosestMultipleAboveThreshold(bus, yourTime)
      
      if first:
         minDiff = diff
         targetBus = bus
      first = False

      if diff < minDiff:
         minDiff = diff
         targetBus = bus
   
   return abs(minDiff - yourTime) * targetBus

def findBusOrder(fullBusSchedule: List[str]) -> (List[List[int]]):
   """
   Finds and returns the bus ordering as a list for which part 2 needs
   """
   busOrder: List[List[int]] = []

   numMinutesLater: int = 0

   for bus in fullBusSchedule:
      if bus.isnumeric():
         busOrder.append([int(bus), numMinutesLater])
      numMinutesLater += 1
   
   return busOrder

def findSpecialTime(busOrder: List[List[int]]) -> int:
   """
   Finds the special time that will have the part 2 solution
   """
   stepVal: int = max(busOrder)[0]
   time: int = stepVal - max(busOrder)[1]

   numTries = 0
   while True:
      if time % busOrder[0][0] == 0:
         num = 0
         for i in range(1, len(busOrder)):
            if ((time + busOrder[i][1]) % busOrder[i][0]) == 0:
               num += 1
            else:
               break
            
            print(f"==={numTries}===")

            if num == len(busOrder) - 1:
               print(f"Time {time}, | iterations: {numTries}")
               return time

      time += stepVal
      numTries += 1

def main():
   inputLines: List[str] = [line.strip() for line in readFile(FILEPATH)]
   yourTime: int = int(inputLines[0])
   onlyValidBuses: List[int] = [int(i) for i in inputLines[1].split(",") if i != "x"]
   # Part 1
   partOne: int = calculateWeightedWaitTime(yourTime, onlyValidBuses)
   print(f"Part 1 -- Time Diff: {partOne}")

   # Part 2
   fullBusSchedule: List[str] = inputLines[1].strip().split(",")
   # print(fullBusSchedule)
   busOrder: List[List[int]] = findBusOrder(fullBusSchedule)
   # findGoldenTime(busOrder)

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""