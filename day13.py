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
   busOrder: List[List[int]] = findBusOrder(fullBusSchedule)
   print(f"Part 2 -- Special Time: TBD")

if __name__ == "__main__":
   main()

"""
--- Day 13: Shuttle Search ---
--- Part One ---
Bus schedules are defined based on a timestamp that measures the number of minutes since some fixed
reference point in the past. At timestamp 0, every bus simultaneously departed from the sea port.
After that, each bus travels to the airport, then various other locations, and finally returns to the
sea port to repeat its journey forever.
The time this loop takes a particular bus is also its ID number: the bus with ID 5 departs from the
sea port at timestamps 0, 5, 10, 15, and so on. The bus with ID 11 departs at 0, 11, 22, 33, and so
on. If you are there when the bus departs, you can ride that bus to the airport!
What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes
you'll need to wait for that bus?
--- Part Two ---
The shuttle company is running a contest: one gold coin for anyone that can find the earliest timestamp
such that the first bus ID departs at that time and each subsequent listed bus ID departs at that
subsequent minute. (The first line in your input is no longer relevant.)
For example, suppose you have the same list of bus IDs as above:
7,13,x,x,59,x,31,19
An x in the schedule means there are no constraints on what bus IDs must depart at that time.
This means you are looking for the earliest timestamp (called t) such that:
    Bus ID 7 departs at timestamp t.
    Bus ID 13 departs one minute after timestamp t.
    There are no requirements or restrictions on departures at two or three minutes after timestamp t.
    Bus ID 59 departs four minutes after timestamp t.
    There are no requirements or restrictions on departures at five minutes after timestamp t.
    Bus ID 31 departs six minutes after timestamp t.
    Bus ID 19 departs seven minutes after timestamp t.
However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than 100000000000000!
What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?
"""