# 12/7/20

from Helpers.FileHelper import readFile
from typing import List, Dict
FILEPATH: str = "2020/Input/day07.txt"

def createBagMap(s: str, keepNumbering: bool) -> Dict[str, List[str]]:
   """
   Creates a bag map from the given string, choose to keep or remove numbering
   """
   s = s[0:-2].strip()
   containIndex: int = s.index("contain")
   
   key: str = s[0:containIndex].strip()[0:-1]
   value: List[str] = s[containIndex+len("contain"):].split(", ")

   # Chomps off number at beginning of string, if user wants
   for i in range(len(value)):
      tempStr: str = value[i]
      for char in range(len(tempStr)):
         if not keepNumbering:
            if tempStr[char] == ' ' or tempStr[char].isdigit():
               continue
            else:
               break
         else:
            if tempStr[char] == ' ':
               continue
            else:
               break
      value[i] = tempStr[char:] if tempStr[-1] != "s" else tempStr[char:-1]

   output: Dict[str, List[str]] = dict()
   output[key] = value
   return output

def containsShinyGoldBag(key: str, bagMap: Dict[str, List[str]]) -> int:
   """
   Recursively sees if the key (a bag) has any gold inside it. Returns 1 if so, 0 otherwise. Part 1
   """
   flag: int = 0

   # Base cases
   if key == "no other bag":
      return 0
   if key == "shiny gold bag":
      return 1

   for val in bagMap[key]:
      flag += containsShinyGoldBag(val, bagMap)
      if flag >= 1:
         break

   return 1 if flag >= 1 else 0

def countNumBagsWithin(key: str, bagMap: Dict[str, List[str]]) -> int:
   """
   Recursively counts number of bags within the key (a bag). Part 2
   """
   count: int = 0

   for val in bagMap[key]:
      if val != "no other bag":
         numSubBag: int = int(val[0])
         count += numSubBag + (numSubBag * countNumBagsWithin(val[2:], bagMap))
   
   return count

def main():
   # Capture input
   bagInput: List[str] = readFile(FILEPATH)
   bagMap: Dict[str, List[str]] = {}

   # Populate hash map of bags
   for s in bagInput:
      bagMap.update(createBagMap(s, False))

   # Part 1
   count = 0
   for key in bagMap.keys():
      count += containsShinyGoldBag(key, bagMap)
   print(f"Part 1 -- Shiny Gold Bag count: {count - 1}")

   # Part 2
   bagMap = bagMap.clear()
   bagMap = {}
   for s in bagInput:
      bagMap.update(createBagMap(s, True))
   numBagsWithin: int = countNumBagsWithin("shiny gold bag", bagMap)
   print(f"Part 2 -- number of bags within Shiny Gold Bag: {numBagsWithin}")

if __name__ == "__main__":
   main()

"""
--- Day 7: Handy Haversacks ---
--- Part One ---
In the above rules, the following options would be available to you:

    A bright white bag, which can hold your shiny gold bag directly.
    A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
    A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
    A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.
How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)
--- Part Two ---
Consider again your shiny gold bag and the rules from the above example:

    faded blue bags contain 0 other bags.
    dotted black bags contain 0 other bags.
    vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
    dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant
plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""