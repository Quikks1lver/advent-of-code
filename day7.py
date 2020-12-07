# 12/7/20

from Helpers.FileHelper import readFile
from typing import List, Dict
FILEPATH: str = "Input/day7.txt"

def createBagMap(s: str) -> Dict[str, List[str]]:
   """
   Creates a bag map from the given string
   """
   s = s[0:-2].strip()
   containIndex: int = s.index("contain")
   
   key: str = s[0:containIndex].strip()[0:-1]
   value: List[str] = s[containIndex+len("contain"):].split(", ")

   # Chomps off number at beginning of string
   for i in range(len(value)):
      tempStr: str = value[i]
      for char in range(len(tempStr)):
         if tempStr[char] == ' ' or tempStr[char].isdigit():
            continue
         else:
            break
      value[i] = tempStr[char:] if tempStr[-1] != "s" else tempStr[char:-1]

   output: Dict[str, List[str]] = dict()
   output[key] = value
   return output

def recursiveGoldCounter(key, bagMap) -> int:
   """
   Recursively sees if the key (a bag) has any gold inside it
   """
   flag: int = 0

   # Base cases
   if key == "no other bag":
      return 0
   if key == "shiny gold bag":
      return 1

   for val in bagMap[key]:
      flag += recursiveGoldCounter(val, bagMap)
      if flag >= 1:
         break

   return 1 if flag >= 1 else 0

def main():
   # Capture input
   input: List[str] = readFile(FILEPATH)
   bagMap: Dict[str, List[str]] = {}

   # Populate hash map of bags
   for s in input:
      bagMap.update(createBagMap(s))

   # Part 1
   count = 0
   for key in bagMap.keys():
      count += recursiveGoldCounter(key, bagMap)
   print(f"Part 1 -- Shiny Gold Bag Count: {count - 1}")

if __name__ == "__main__":
   main()