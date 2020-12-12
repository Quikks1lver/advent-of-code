# 12/12/20

from Helpers.FileHelper import readFile
from typing import List
from enum import Enum
FILEPATH: str = "Input/day12.txt"

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
   
   def moveRelativeToWaypoint(self, unitPayload: int, wayPointHoriz: int, wayPointVert: int) -> None:
      """
      Moves ferry relative to the waypoint
      """
      horizPayload: int = unitPayload * wayPointHoriz
      vertPayload: int = unitPayload * wayPointVert
      self.horiz += horizPayload
      self.vert += vertPayload

class Waypoint():
   """
   Represents a waypoint
   """
   def __init__(self, horiz: int, vert: int):
      self.horiz = horiz
      self.vert = vert
   
   def consumeWaypointInstruction(self, instruction: str) -> None:
      """
      Takes an instruction and mutates waypoint state
      """
      iType: str = instruction[0]

      if iType == "R" or iType == "L":
         # rotational
         rotation: int = int(instruction[1:])
         rotation = int(rotation / 90)
         if rotation == 1:
            if iType == "R":
               self.horiz, self.vert = self.vert, -1 * self.horiz
            else:
               self.horiz, self.vert = -1 * self.vert, self.horiz
         elif rotation == 2:
            self.horiz, self.vert = -1 * self.horiz, -1 * self.vert
         else:
            if iType == "R":
               self.horiz, self.vert = -1 * self.vert, self.horiz
            else:
               self.horiz, self.vert = self.vert, -1 * self.horiz
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
            print("ERROR, Forward not supported for waypoint")

def main():
   instructions: List[str] = [i.strip() for i in readFile(FILEPATH)]

   # Part 1
   boat: Ferry = Ferry(Direction.EAST, 0, 0)
   for i in instructions:
      boat.consumeInstruction(i)
   print(f"Part 1 -- Manhattan Distance: {boat.calculateManhattanDistance()}")

   # Part 2
   boat = Ferry(Direction.EAST, 0, 0)
   wayPoint: Waypoint = Waypoint(10, 1)
   for i in instructions:
      if i[0] == Direction.FORWARD.value:
         boat.moveRelativeToWaypoint(int(i[1:]), wayPoint.horiz, wayPoint.vert)
      else:
         wayPoint.consumeWaypointInstruction(i)
   print(f"Part 2 -- Manhattan Distance: {boat.calculateManhattanDistance()}")

if __name__ == "__main__":
   main()

"""
--- Day 12: Rain Risk ---
--- Part One ---
Unfortunately, the ship's navigation computer seems to be malfunctioning; rather than giving a route
directly to safety, it produced extremely circuitous instructions. When the captain uses the PA system
to ask if anyone can help, you quickly volunteer.
    Action N means to move north by the given value.
    Action S means to move south by the given value.
    Action E means to move east by the given value.
    Action W means to move west by the given value.
    Action L means to turn left the given number of degrees.
    Action R means to turn right the given number of degrees.
    Action F means to move forward by the given value in the direction the ship is currently facing.
Figure out where the navigation instructions lead. What is the Manhattan distance between that location
and the ship's starting position?
--- Part Two ---
Before you can give the destination to the captain, you realize that the actual action meanings were
printed on the back of the instructions the whole time.
Almost all of the actions indicate how to move a waypoint which is relative to the ship's position:
    Action N means to move the waypoint north by the given value.
    Action S means to move the waypoint south by the given value.
    Action E means to move the waypoint east by the given value.
    Action W means to move the waypoint west by the given value.
    Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
    Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
    Action F means to move forward to the waypoint a number of times equal to the given value.
Figure out where the navigation instructions actually lead. What is the Manhattan distance between
that location and the ship's starting position?
"""