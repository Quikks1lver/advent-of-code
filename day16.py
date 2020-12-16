# 12/16/20

from Helpers.FileHelper import readFile, readFileWithEmptyLineBreaks
from typing import List
import re
FILEPATH: str = "Input/day16.txt"

class Field:
   """
   Represents a field from the problem, with a name and accepted range(s) of values
   """
   def __init__(self, name: str, lowerBound1: int, upperBound1: int, lowerBound2: int, upperBound2: int):
      self.name = name
      self.lowerBound1 = lowerBound1
      self.upperBound1 = upperBound1
      self.lowerBound2 = lowerBound2
      self.upperBound2 = upperBound2
   
   def isValidNum(self, num: int) -> bool:
      """
      Returns True if num is valid in the range, False otherwise
      """
      if (num >= self.lowerBound1 and num <= self.upperBound1) or (num >= self.lowerBound2 and num <= self.upperBound2):
         return True
      return False
   
   def __repr__(self):
      return f"{self.name} -- ({self.lowerBound1}, {self.upperBound1}) , ({self.lowerBound2}, {self.upperBound2})"

def constructFieldsList(rawInfo: List[str]) -> List[Field]:
   """
   Constructs a fields list from raw input
   """
   fieldRegex = re.compile(r"(\w*:) (\d*-\d*) or (\d*-\d*)")
   fieldsList: List[Field] = []
   name: str = ""
   lowerBound1: int = 0
   upperBound1: int = 0
   lowerBound2: int = 0
   upperBound2: int = 0

   for s in rawInfo:
      mo = fieldRegex.search(s)
      name = mo.group(1).rstrip(":")
      
      bound: List[int] = mo.group(2).split("-")
      lowerBound1, upperBound1 = int(bound[0]), int(bound[1])
      
      bound: List[int] = mo.group(3).split("-")
      lowerBound2, upperBound2 = int(bound[0]), int(bound[1])

      tempField: Field = Field(name, lowerBound1, upperBound1, lowerBound2, upperBound2)
      fieldsList.append(tempField)
   
   return fieldsList

def calculateErrorRate(fieldsList: List[Field], nearbyTickets: List[str]) -> int:
   """
   Calculates ticket scanning error rate
   """
   sum: int = 0

   for ticket in nearbyTickets:
      nums: List[int] = [int(t) for t in ticket.split(",")]

      for x in nums:
         flag: bool = True
         
         for field in fieldsList:
            if field.isValidNum(x):
               flag = False
               break
         
         if flag:
            sum += x
   
   return sum

def main():
   allInputLines: List[str] = readFileWithEmptyLineBreaks(FILEPATH)
   
   fieldsInput: List[str] = allInputLines[0].split("\n")
   yourTicketInput: str = allInputLines[1].split("\n")[1].strip()
   nearbyTicketInput: List[str] = [s.strip() for s in allInputLines[2].split("\n")[1:]]

   fieldsList: List[Field] = constructFieldsList(fieldsInput)
   
   # Part 1
   print(f"Part 1 -- Error Rate: {calculateErrorRate(fieldsList, nearbyTicketInput)}")

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""