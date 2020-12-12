# 12/12/20

from Helpers.FileHelper import readFile
from typing import List
from enum import Enum
FILEPATH: str = "Input/day12.txt"

DEBUGGING: bool = False

class Direction(Enum):
   """
   Cardinal direction
   """
   NORTH = "N"
   EAST = "E"
   SOUTH = "S"
   WEST = "W"
   FORWARD = "F"

class Ferry:
   """
   Represents a ferry
   """
   DIRECTIONS_CIRCLE: List[Direction] = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

   def __init__(self, curDirection: Direction, horiz: int, vert: int):
      self.curDirection = curDirection
      self.horiz = horiz
      self.vert = vert

   def moveFerryForward(self, payload: int) -> None:
      """
      Moves ferry forward by set amount
      """
      if self.curDirection == Direction.NORTH:
         self.vert += payload
      elif self.curDirection == Direction.EAST:
         self.horiz += payload
      elif self.curDirection == Direction.SOUTH:
         self.vert -= payload
      else:
         self.horiz -= payload

   def consumeInstruction(self, instruction: str) -> None:
      """
      Takes an instruction and mutates Ferry state
      """
      iType: str = instruction[0]

      if iType == "R" or iType == "L":
         # rotational
         rotation: int = int(instruction[1:])
         rotation /= 90
         oldIndex: int = Ferry.DIRECTIONS_CIRCLE.index(self.curDirection)
         if iType == "R":
            newIndex: int = int((oldIndex + rotation) % len(Ferry.DIRECTIONS_CIRCLE))
         else:
            newIndex: int = int((oldIndex - rotation + len(Ferry.DIRECTIONS_CIRCLE)) % len(Ferry.DIRECTIONS_CIRCLE))
         self.curDirection = Ferry.DIRECTIONS_CIRCLE[newIndex]
      else:
         payload: int = int(instruction[1:])
         # directional or forward
         if iType == Direction.NORTH.value:
            self.vert += payload
         elif iType == Direction.EAST.value:
            self.horiz += payload
         elif iType == Direction.SOUTH.value:
            self.vert -= payload
         elif iType == Direction.WEST.value:
            self.horiz -= payload
         else:
            self.moveFerryForward(payload)
   
   def calculateManhattanDistance(self) -> int:
      """
      Calculates and returns manhattan distance of the ferry
      """
      return abs(self.horiz) + abs(self.vert)

def main():
   instructions: List[str] = [i.strip() for i in readFile(FILEPATH)]

   boat: Ferry = Ferry(Direction.EAST, 0, 0)

   # Part 1
   for i in instructions:
      boat.consumeInstruction(i)
      if DEBUGGING:
         print(f" {i} | {boat.horiz} {boat.vert} {boat.curDirection.value} ")
   print(f"Part 1 -- Manhattan Distance: {boat.calculateManhattanDistance()}")

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""