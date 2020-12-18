# 12/17/20

from Helpers.AOC import whiteFlag
from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/day17.txt"

def main():
   # As of 12/18, I'll come back to this tricky problem at a later date.

   # Part 1
   whiteFlag(1, "num cubes", "12/18")

   # Part 2
   whiteFlag(2, "num cubes", "12/18")

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
TBD
"""