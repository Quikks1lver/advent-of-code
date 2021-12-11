# 12/14/20

from Helpers.Binary import convertBinaryToDecimal, convertDecimalToBitString # for testing
from Helpers.FileHelper import readFile
from itertools import product
from typing import Dict, List, Union
FILEPATH: str = "2020/Input/day14.txt"

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

def maskToXMap(s: str) -> Dict[int, Union[str, int]]:
   """
   Creates a maskmap from an address mask and transforms it into a mask map, keeps Xs
   """
   maskXMap: Dict[int, Union[str, int]] = dict()
   power: int = 1

   for i in range(len(s) - 1, -1, -1):
      if s[i] != '0':
         maskXMap[power] = s[i] if s[i] == "X" else int(s[i])
      power = power << 1

   return maskXMap

def constructAddressList(addressMap: Dict[int, int], maskXMap: Dict[int, Union[str, int]]) -> List[int]:
   """
   Constructs a memory address list from an address map and an X map
   """
   num: int = 0
   addressList: List[int] = []
   variables: List[int] = []

   for i in range(NUM_BITS - 1, -1, -1):
      power: int = 2 ** i
      if power in maskXMap:
         if maskXMap[power] == 1:
            num += (power * maskXMap[power])
         else:
            variables.append(power)
      elif power in addressMap:
         num += (power * addressMap[power])

   # essentially makes a truth table
   # i got the idea from https://stackoverflow.com/questions/29548744/creating-a-truth-table-for-any-expression-in-python
   states = list(product([True, False], repeat=len(variables)))

   for state in states:
      addr: int = num
      for i in range(len(state)):
         if state[i] == True:
            addr += variables[i]
      addressList.append(addr)

   if len(addressList) == 0:
      addressList.append(num)
   return addressList

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

def sumValues(map: dict) -> int:
   """
   Sums dict's values
   """
   total: int = 0
   for v in map.values():
      total += v
   return total

def parseMasksForNumbers(inputLines: List[str]) -> int:
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

   return sumValues(memory)

def parseMasksForAddresses(inputLines: List[str]) -> int:
   """
   Parses input and returns sum of whatever's left over in memory at the end
   """
   maskXMap: Dict[int, Union[str, int]] = dict()
   addressMap: Dict[int, int] = dict()
   memory: Dict[int, int] = dict()
   addressList: List[int] = []

   for line in inputLines:
      if line[0:4] == "mask":
         maskXMap.clear()
         maskXMap = maskToXMap(line[7:])
      else:
         addressMap.clear()
         addressList.clear()

         num: str = line.split(" = ")[1]
         memAddress: int = int(line.split(" = ")[0].lstrip("mem[").rstrip("]"))
         addressMap = maskToMap(memAddress, False)
         addressList = constructAddressList(addressMap, maskXMap)

         for address in addressList:
            memory[address] = int(num)

   return sumValues(memory)

def main():
   inputLines: List[str] = [line.strip() for line in readFile(FILEPATH)]

   # Part 1
   total: int = parseMasksForNumbers(inputLines)
   print(f"Part 1 -- Total left in memory: {total}")

   # Part 2
   total: int = parseMasksForAddresses(inputLines)
   print(f"Part 2 -- Total left in memory: {total}")

if __name__ == "__main__":
   main()

"""
--- Day 14: Docking Data ---
--- Part One ---
As your ferry approaches the sea port, the captain asks for your help again. The computer system that
runs this port isn't compatible with the docking program on the ferry, so the docking parameters aren't
being correctly initialized in the docking program's memory.
The initialization program (your puzzle input) can either update the bitmask or write a value to memory.
Values and memory addresses are both 36-bit unsigned integers. For example, ignoring bitmasks for a
moment, a line like mem[8] = 11 would write the value 11 to memory address 8.
The bitmask is always given as a string of 36 bits, written with the most significant bit (representing
2^35) on the left and the least significant bit (2^0, that is, the 1s bit) on the right. The current
bitmask is applied to values immediately before they are written to memory: a 0 or 1 overwrites the
corresponding bit in the value, while an X leaves the bit in the value unchanged.
Execute the initialization program. What is the sum of all values left in memory after it completes?
--- Part Two ---
A version 2 decoder chip doesn't modify the values being written at all. Instead, it acts as a memory
address decoder. Immediately before a value is written to memory, each bit in the bitmask modifies the
corresponding bit of the destination memory address in the following way:
    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably. In practice, this
means the floating bits will take on all possible values, potentially causing many memory addresses
to be written all at once!
Execute the initialization program using an emulator for a version 2 decoder chip. What is the sum
of all values left in memory after it completes?
"""