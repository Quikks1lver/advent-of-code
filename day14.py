# 12/14/20

from Helpers.Binary import convertBinaryToDecimal, convertDecimalToBitString # for testing
from Helpers.FileHelper import readFile
from typing import Dict, List
FILEPATH: str = "Input/day14.txt"

NUM_BITS: int = 36

def maskToMap(s: str, isMask: bool) -> Dict[int, int]:
   """
   Creates a maskmap from a string (number or a mask) and transforms it into a mask map
   """
   maskMap: Dict[int] = dict()
   power: int = 1

   if not isMask:
      bitString: str = convertDecimalToBitString(s)
      s = bitString

   for i in range(len(s) - 1, -1, -1):
      if s[i] != "X":
         maskMap[power] = int(s[i])
      power = power << 1

   return maskMap

def unmask(numMap: Dict[int, int], maskMap: Dict[int, int]) -> int:
   """
   Given a number map and a mask's map, find the masked number
   """
   num: int = 0

   for i in range(NUM_BITS - 1, -1, -1):
      power: int = 2 ** i
      if power in maskMap:
         num += (power * maskMap[power])
      elif power in numMap:
         num += (power * numMap[power])

   return num

def parseInput(inputLines: List[str]) -> int:
   """
   Parses input and returns sum of whatever's left over in memory at the end
   """
   maskMap: Dict[int, int] = dict()
   numMap: Dict[int, int] = dict()
   memory: Dict[int, int] = dict()

   for line in inputLines:
      if line[0:4] == "mask":
         maskMap.clear()
         maskMap = maskToMap(line[7:], True)
      else:
         num: str = line.split(" = ")[1]
         memAddress: int = int(line.split(" = ")[0].lstrip("mem[").rstrip("]"))
         numMap.clear()
         numMap = maskToMap(num, False)
         memory[memAddress] = unmask(numMap, maskMap)

   total: int = 0
   for v in memory.values():
      total += v
   
   return total               

def main():
   inputLines: List[str] = [line.strip() for line in readFile(FILEPATH)]

   # Part 1
   total: int = parseInput(inputLines)
   print(f"Part 1 -- Total left in memory: {total}")

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""