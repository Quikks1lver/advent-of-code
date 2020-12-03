# 12/3/20

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/inputThree.txt"

def buildMountain(filename: str) -> List[str]:
   """
   Constructs the mountain based on file input
   """
   return [line.strip() for line in readFile(filename)]

def findTreesOnMountainDescent(mountain: List[str], dx: int, dy: int) -> int:
   """
   Finds the trees hit while descending the mountain, based on dx/dy "slope"
   """
   rowIndex, colIndex = 0, 0
   rowEnd = len(mountain)
   colLength = len(mountain[0])
   TREE: str = "#"
   treeCount: int = 0

   while rowIndex < rowEnd:
      if mountain[rowIndex][colIndex % colLength] == TREE:
         treeCount += 1

      colIndex += dy
      rowIndex += dx
   
   print(f"You will run into {treeCount} trees.")
   return treeCount
   
   
def main():
   mountain: List[str] = buildMountain(FILEPATH)

   # part 1
   findTreesOnMountainDescent(mountain, 1, 3)

   # part 2
   slopes: List[List[int]] = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
   productOfTrees: int = 1
   for slope in slopes:
      productOfTrees *= findTreesOnMountainDescent(mountain, slope[0], slope[1])

   print(f"\nProduct of trees: {productOfTrees}")

if __name__ == "__main__":
    main()

"""
--- Day 3: Toboggan Trajectory ---
--- Part One ---
Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""