# --- Day 3: Toboggan Trajectory ---
# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/inputThree.txt"

def buildMountain(filename: str) -> List[str]:
   """
   Constructs the mountain based on file input
   """
   fileInput: List[str] = readFile(filename)
   mountain: List[str] = []
   
   for line in fileInput:
      mountain.append(line.strip())
   
   return mountain

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
   # part 1
   findTreesOnMountainDescent(buildMountain(FILEPATH), 1, 3)

   # part 2
   slopes: List[List[int]] = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
   productOfTrees: int = 1
   for slope in slopes:
      productOfTrees *= findTreesOnMountainDescent(buildMountain(FILEPATH), slope[0], slope[1])

   print(f"\nProduct of trees: {productOfTrees}")

if __name__ == "__main__":
    main()