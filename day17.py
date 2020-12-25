# 12/17/20

from enum import Enum
from Helpers.AOC import whiteFlag
from Helpers.FileHelper import readFile
from typing import List, Set, Tuple
FILEPATH: str = "Input/day17.txt"

class Status(Enum):
   """
   Cube activity status
   """
   ACTIVE = "#"
   INACTIVE = "."

def createActiveSet(strList: List[str]) -> Set[Tuple[int, int, int]]:
   """
   Given a list of string input, returns a set of active conway cubes
   """
   activeSet: Set[Tuple[int, int, int]] = set()

   for y, line in enumerate(strList):
      for x, ch in enumerate(line):
         if ch == Status.ACTIVE.value:
            activeSet.add( (x, y, 0) )
   
   return activeSet

def countActiveCubesAfterXCycles(activeSet: Set[Tuple[int, int, int]], cycles: int) -> int:
   """
   Runs X cycles of the process according to the below rules, and outputs num active cubes:
   - If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
     Otherwise, the cube becomes inactive.
   - If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise,
     the cube remains inactive.
   """
   for _ in range(cycles):
      newSet: Set[Tuple[int, int, int]] = activeSet.copy()
      cubesToCheck: Set[Tuple[int, int, int]] = set()
      
      for (x, y, z) in activeSet:
         cubesToCheck.add( (x, y, z) )
         
         for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
               for dz in range(-1, 2, 1):
                  cubesToCheck.add( (x + dx, y + dy, z + dz) )
         
      for (x, y, z) in cubesToCheck:
         numActiveCubes: int = 0
         
         for dx in range(-1, 2, 1):
            for dy in range(-1, 2, 1):
               for dz in range(-1, 2, 1):
                  if dx != 0 or dy != 0 or dz != 0:
                     newX, newY, newZ = x + dx, y + dy, z + dz

                     if (newX, newY, newZ) in activeSet:
                        numActiveCubes += 1
         
         if (x, y, z) in activeSet and numActiveCubes in {2, 3}:
            newSet.add( (x, y, z) )
         
         if (x, y, z) in activeSet and numActiveCubes not in {2, 3}:
            newSet.remove( (x, y, z) )
         
         if (x, y, z) not in activeSet and numActiveCubes == 3:
            newSet.add( (x, y, z) )
      
      activeSet = newSet
   
   return len(activeSet)

def main():
   # After completing day 24, I decided to give this puzzle another go . . .
   # Again, credits to Jonathan Paulson for helping me understand how to approach these puzzles,
   # as in day 24.
   
   # Part 1
   inputLines: List[str] = [s.strip() for s in readFile(FILEPATH)]
   
   activeSet = createActiveSet(inputLines)
   print(f"Part 1 -- Active Cubes after 6 cycles: {countActiveCubesAfterXCycles(activeSet, 6)}")

   # Part 2
   # whiteFlag(2, "num cubes", "12/18")

if __name__ == "__main__":
   main()

"""
--- Day 17: Conway Cubes ---
--- Part One ---
The experimental energy source is based on cutting-edge technology: a set of Conway Cubes contained
in a pocket dimension! When you hear it's having problems, you can't help but agree to take a look.
The pocket dimension contains an infinite 3-dimensional grid. At every integer 3-dimensional coordinate
(x,y,z), there exists a single cube which is either active or inactive.
During a cycle, all cubes simultaneously change their state according to the following rules:
   - If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
     Otherwise, the cube becomes inactive.
   - If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. Otherwise,
     the cube remains inactive.
Starting with your given initial configuration, simulate six cycles. How many cubes are left in the
active state after the sixth cycle?
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy source engineers expected.
Apparently, the pocket dimension actually has four spatial dimensions, not three.
"""