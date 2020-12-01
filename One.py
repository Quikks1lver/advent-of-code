# 12/1/20
# --- Day 1: Report Repair ---
#
# --- Part One ---
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
#
# --- Part Two ---
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin
# they had left over from a past vacation. They offer you a second one if you can find three numbers
# in your expense report that meet the same criteria.
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.
# In your expense report, what is the product of the three entries that sum to 2020?

from FileHelper import readFile
import sys

FILENAME: str = "Input/inputOne.txt"
MORE_OUTPUT: bool = False

def populateDictWithNumbers(filename: str) -> dict:
   """
   Opens a file consisting of numbers and populates and returns a dictionary/hash set containing them
   """

   numsDict: dict = {}

   try:
      numsList: list = readFile(FILENAME)
      
      for num in numsList:
         key = int(num)
         numsDict.setdefault(key, 1)
      
      return numsDict
   except:
      raise Exception(f"Could not load file at {filename}")

def findSumOperands(numsDict: dict, targetNum: int) -> (int, int):
   """
   Given a dictionary of integers and a target, finds which integers sum to the given number
   and returns these two integers. If no such integers sum to the given number,
   return maximum possible integer
   """
   
   # input validation   
   if numsDict == None:
      return sys.maxsize, sys.maxsize
   
   for key in numsDict.keys():
      if targetNum - key in numsDict:
         if MORE_OUTPUT:
            print(f"{key} and {targetNum - key}")
         return key, targetNum - key

   # Failure: return maxsize
   return sys.maxsize, sys.maxsize

def findThreeOperands(numsDict: dict, targetNum: int) -> (int, int, int):
   """
   Similar to findSumOperands, given a dictionary of integers and a target, finds which 3
   integers sum to the given number. If no such integers sum to the given number,
   return maximum possible integer
   """

   # input validation
   if numsDict == None:
      return sys.maxsize, sys.maxsize, sys.maxsize
   
   for op1 in numsDict.keys():
      firstTarget = targetNum - op1
      op2, op3 = findSumOperands(numsDict, firstTarget)
      if op2 != sys.maxsize and op3 != sys.maxsize:
         return op1, op2, op3

   return sys.maxsize, sys.maxsize, sys.maxsize

""" Call the functions! """
numsDict: dict = populateDictWithNumbers(FILENAME)
# Find part one answers
print(f"Part one operands: {findSumOperands(numsDict, 2020)}")
# Find part two answers
print(f"Part two operands: {findThreeOperands(numsDict, 2020)}")