# 12/9/20

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "2020/Input/day09.txt"

def canTwoSum(numsList: List[int], target: int) -> bool:
   """
   If two numbers in the list can add to target, return True, else, False
   """
   for x in numsList:
      targetNum = target - x
      if targetNum in numsList:
         return True
   return False

def findOddball(numsList: List[int], preambleLength: int) -> int:
   """
   Finds the first number in the list which cannot be found by summing the
   previous n numbers, where n is preambleLength
   """
   preambleList: List[int] = numsList[0:preambleLength]
   listLength: int = len(numsList)
   success: bool = False

   for i in range(preambleLength, listLength, 1):
      if i != preambleLength:
         preambleList.pop(0)
         preambleList.append(numsList[i - 1])
      
      possibleOddball: int = numsList[i]

      if not canTwoSum(preambleList, possibleOddball):
         return possibleOddball

def findEncryptionWeakness(numsList: List[int], oddball: int) -> int:
   """
   Finds a contiguous set of numbers that add to oddball, and returns
   the sum of this list's largest and smallest values
   """
   encryptionList: List[int] = []
   length: int = len(numsList)
   curSum: int = 0
   success: bool = False

   for i in range(length):
      encryptionList.clear()
      encryptionList = []
      encryptionList.append(numsList[i])
      curSum = numsList[i]

      for j in range(i + 1, length, 1):
         curSum += numsList[j]
         encryptionList.append(numsList[j])
         
         if curSum == oddball:
            success = True
            break
      
      if success:
         break
   
   encryptionList.sort()
   return encryptionList[-1] + encryptionList[0]


def main():
   numsList: List[int] = [int(s.strip()) for s in readFile(FILEPATH)]

   # Part 1
   oddball: int = findOddball(numsList, 25)
   print(f"Part 1 -- Oddball: {oddball}")

   # Part 2
   weakness: int = findEncryptionWeakness(numsList, oddball)
   print(f"Part 2 -- Encryption Weakness: {weakness}")

if __name__ == "__main__":
   main()

"""
--- Day 9: Encoding Error ---
--- Part One ---
XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be
the sum of any two of the 25 immediately previous numbers. The two numbers will have different values,
and there might be more than one such pair.
The first step of attacking the weakness in the XMAS data is to find the first number in the list
(after the preamble) which is not the sum of two of the 25 numbers before it. What is the first
number that does not have this property?
--- Part Two ---
The final step in breaking the XMAS encryption relies on the invalid number you just found: you must
find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.
In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1,
127. (Of course, the contiguous set of numbers in your actual list might be much longer.)
To find the encryption weakness, add together the smallest and largest number in this contiguous
range. What is the encryption weakness in your XMAS-encrypted list of numbers?
"""