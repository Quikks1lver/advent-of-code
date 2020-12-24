# 12/24/20

from enum import Enum
from Helpers.FileHelper import readFile
from typing import List, Set, Tuple
FILEPATH: str = "Input/day24.txt"

class HexDirections(Enum):
   """
   6 hexagonal directions
   """
   E = "e"
   W = "w"
   NW = "nw"
   NE = "ne"
   SW = "sw"
   SE = "se"

def tokenizeHexString(s: str) -> Tuple[int, int, int]:
   """
   Turns a string into a token
   """
   
   # to create hexagonal "points", I consulted this website which taught me how to translate hexagonal
   # directions to a simple x, y, z coordinate scheme: https://www.redblobgames.com/grids/hexagons/
   x, y, z = 0, 0, 0
   
   i = 0
   while i < len(s):
      if s[i] == HexDirections.E.value:
         x += 1
         y -= 1
         i += 1
      elif s[i] == HexDirections.W.value:
         x -= 1
         y += 1
         i += 1
      elif s[i:i+2] == HexDirections.NE.value:
         x += 1
         z -= 1
         i += 2
      elif s[i:i+2] == HexDirections.NW.value:
         y += 1
         z -= 1
         i += 2
      elif s[i:i+2] == HexDirections.SE.value:
         y -= 1
         z += 1
         i += 2
      else: # SW
         x -= 1
         z += 1
         i += 2
   
   return (x, y, z)

def countBlackTiles(tiles: List[Tuple[int, int, int]]) -> int:
   """
   Counts how many tiles are turned over (black tiles)
   """
   blackTiles: Set[HexTile] = set()

   for tile in tiles:
      if tile in blackTiles:
         blackTiles.remove(tile)
      else:
         blackTiles.add(tile)
   
   return len(blackTiles)

def main():
   inputLines: List[str] = [s.strip() for s in readFile(FILEPATH)]   
   tiles: List[Tuple[int, int, int]] = [tokenizeHexString(line) for line in inputLines]

   # Part 1
   print(f"Part 1 -- Number of black tiles: {countBlackTiles(tiles)}")

   # Part 2
   # TBD

if __name__ == "__main__":
   main()

"""
--- Day 24: Lobby Layout ---
--- Part One ---
Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator.
You make your way to the resort. As you enter the lobby, you discover a small problem: the floor is being
renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.
The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern.
Not in the mood to wait, you offer to help figure out the pattern.
The tiles are all white on one side and black on the other. They start with the white side facing up.
The lobby is large enough to fit whatever pattern might need to appear there.
A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input).
Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting
from a reference tile in the very center of the room. (Every line starts from the same reference tile.)
Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest,
and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A
tile is identified by a series of these directions with no delimiters; for example, esenee identifies
the tile you land on if you start at the reference tile and then move one tile east, one tile southeast,
one tile northeast, and one tile east.
--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped
according to the following rules:
    - Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    - Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile in question.
The rules are applied simultaneously to every tile; put another way, it is first determined which tiles
need to be flipped, then they are all flipped at the same time.
How many tiles will be black after 100 days?
"""