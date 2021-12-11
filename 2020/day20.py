# 12/20/20

from Helpers.AOC import whiteFlag
from Helpers.FileHelper import readFile, readFileWithEmptyLineBreaks
import re
from typing import List
FILEPATH: str = "2020/Input/day20.txt"

class Tile:
   """
   Represents a tile from the input
   """
   def __init__(self, identification: int, pixels: List[str]):
      tempRight: str = ""
      tempLeft: str = ""
      for line in pixels:
         tempLeft += line[0]
         tempRight += line[-1]
      
      self.identification: int = identification
      self.top: str = pixels[0]
      self.bottom: str = pixels[-1]
      self.pixels: List[str] = pixels
      self.right: str = tempRight
      self.left: str = tempLeft
   
   def countNumSharedBorders(self, otherTile) -> (bool, bool, bool, bool):
      """
      Counts how many borders the tile has with another tile, returns 4 bools in the order: T, B, L, R
      """
      numShared: int = 0
      top, bottom, left, right = False, False, False, False, 
      
      if doBordersMatch(self.top, otherTile.top) or doBordersMatch(self.top, otherTile.bottom) or doBordersMatch(self.top, otherTile.left) or doBordersMatch(self.top, otherTile.right):
         top = True
      if doBordersMatch(self.bottom, otherTile.top) or doBordersMatch(self.bottom, otherTile.bottom) or doBordersMatch(self.bottom, otherTile.left) or doBordersMatch(self.bottom, otherTile.right):
         bottom = True
      if doBordersMatch(self.left, otherTile.top) or doBordersMatch(self.left, otherTile.bottom) or doBordersMatch(self.left, otherTile.left) or doBordersMatch(self.left, otherTile.right):
         left = True
      if doBordersMatch(self.right, otherTile.top) or doBordersMatch(self.right, otherTile.bottom) or doBordersMatch(self.right, otherTile.left) or doBordersMatch(self.right, otherTile.right):
         right = True

      return top, bottom, left, right
   
   def __repr__(self):
      return f"{self.identification} -- Top: {self.top} | Bottom: {self.bottom} | Left: {self.left} | Right: {self.right}"

def doBordersMatch(s1: str, s2: str) -> bool:
   """
   Returns True if a border equals another, normally or reversed.
   This taught me how to use this OP slice [::-1]:
   https://www.javatpoint.com/how-to-reverse-a-string-in-python
   """
   if s1 == s2 or s1 == s2[::-1]:
      return True
   return False

def calculateFourCornersProduct(tiles: List[Tile]) -> int:
   """
   Finds 4 corners tiles and multiplies IDs
   """
   fourCornersProduct: int = 1
   for i in range(len(tiles)):
      top, bottom, left, right = False, False, False, False

      for j in range(len(tiles)):
         if i == j:
            continue

         tempTop, tempBottom, tempLeft, tempRight = tiles[i].countNumSharedBorders(tiles[j])
         top, bottom, left, right = top or tempTop, bottom or tempBottom, left or tempLeft, right or tempRight
      
      sharedBorders = 0
      if top == True:
         sharedBorders += 1
      if bottom == True:
         sharedBorders += 1
      if left == True:
         sharedBorders += 1
      if right == True:
         sharedBorders += 1
      
      # The key to this problem is that corner tiles only have *2* adjacencies in this square grid
      if sharedBorders == 2:
         fourCornersProduct *= tiles[i].identification

   return fourCornersProduct

def main():
   inputLines: List[str] = readFileWithEmptyLineBreaks(FILEPATH)
   identificationRegex = re.compile(r"(Tile) (\d*)")
   tiles: List[Tile] = []

   for line in inputLines:
      tileInfo: List[str] = [l.strip() for l in line.split("\n")]
      identificationInfo: int = int(identificationRegex.match(tileInfo[0])[2])
      tiles.append(Tile(identificationInfo, tileInfo[1:]))

   # Part 1
   print(f"Part 1 -- 4 Corners Product: {calculateFourCornersProduct(tiles)}")

   # Part 2
   whiteFlag(2, "Roughness", "12/20")

if __name__ == "__main__":
   main()

"""
--- Day 20: Jurassic Jigsaw ---
--- Part One ---
After decoding the satellite messages, you discover that the data actually contains many small images
created by the satellite's camera array. The camera array consists of many cameras; rather than produce
a single square image, they produce many smaller square image tiles that need to be reassembled back
into a single image.
By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent
borders to line up.
Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?
--- Part Two ---
Now, you're ready to check the image for sea monsters.
The borders of each tile are not part of the actual image; start by removing them.
Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also,
you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the
above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters
(marked with O).
Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are
not part of a sea monster. In the above example, the habitat's water roughness is 273.
How many # are not part of a sea monster?
"""