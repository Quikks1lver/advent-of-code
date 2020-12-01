# --- Day 1: Report Repair ---
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input);
# apparently, something isn't quite adding up. Specifically, they need you to find the two entries
# that sum to 2020 and then multiply those two numbers together.
# For example, suppose your expense report contained the following:
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

import sys

FILENAME: str = "./input.txt"
MORE_OUTPUT: bool = False

def populateDictWithNumbers(filename: str) -> dict:
   """
   Opens a file consisting of numbers and populates and returns a dictionary/hash set containing them
   """

   numsDict: dict = {}

   try:
      with open(filename, "r") as fp:
         numsList: list = fp.readlines()

         for num in numsList:
            key = int(num)
            numsDict.setdefault(key, 1)
      
      return numsDict
   except:
      raise Exception(f"Could not load file at {filename}")

def findSum(numsDict: dict, targetNum: int) -> int:
   """
   Given a dictionary of integers and a target, finds which integers sum to the given number
   and returns the product of these two integers. If no such integers sum to the given number,
   return maximum possible integer
   """
   
   # input validation   
   if numsDict == None:
      return sys.maxsize
   
   for key in numsDict.keys():
      if targetNum - key in numsDict:
         if MORE_OUTPUT:
            print(f"{key} and {targetNum - key}")
         return key * (targetNum - key)

   # Failure: return maxsize
   return sys.maxsize

numsDict: dict = populateDictWithNumbers(FILENAME)
print(findSum(numsDict, 2020))