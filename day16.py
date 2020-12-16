# 12/16/20

from Helpers.AOC import whiteFlag
from Helpers.FileHelper import readFileWithEmptyLineBreaks
from typing import List, Set
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

def constructValidTicketList(fieldsList: List[Field], nearbyTickets: List[str]) -> int:
   """
   Finds invalid tickets and removes them entirely. Returns new, curated, good tickets
   """
   goodTicketList: List[str] = []

   goodOne: bool = True
   for ticket in nearbyTickets:
      goodOne = True
      nums: List[int] = [int(t) for t in ticket.split(",")]

      for x in nums:
         flag: bool = True
         
         for field in fieldsList:
            if field.isValidNum(x):
               flag = False
               break
         
         if flag:
            goodOne = False
      
      if goodOne:
         goodTicketList.append(ticket)
   
   return goodTicketList

def determineFieldTicketRelationships(fieldsList: List[Field], rawTicketInput: List[str]) -> List[str]:
   """
   Determines which fields map to which ticket answers, outputs list
   """
   goodTicketsAsStrings: List[str] = constructValidTicketList(fieldsList, rawTicketInput)
   goodTicketsAsNums: List[List[int]] = []
   for ticket in goodTicketsAsStrings:
      goodTicketsAsNums.append([int(x) for x in ticket.split(",")])

   validFieldsSoFar: Set[int] = set()
   first: bool = True

   outputArr: List[str] = [0] * len(goodTicketsAsNums[0])

   for col in range(len(goodTicketsAsNums[0])):
      validFieldsSoFar.clear()
      first = True
      
      for row in range(len(goodTicketsAsNums)):
         element: int = goodTicketsAsNums[row][col]
         
         if first:
            for i in range(len(fieldsList)):
               if fieldsList[i].isValidNum(element):
                  validFieldsSoFar.add(i)
            first = False

         else:
            tempSet: Set[int] = validFieldsSoFar.copy()

            for i in validFieldsSoFar:
               if not fieldsList[i].isValidNum(element):
                  tempSet.remove(i)

            validFieldsSoFar = tempSet

      if len(validFieldsSoFar) == 1:
         outputArr[col] = list(validFieldsSoFar)[0]
      else:
         outputArr[col] = list(validFieldsSoFar)

   return outputArr

def main():
   allInputLines: List[str] = readFileWithEmptyLineBreaks(FILEPATH)
   
   fieldsInput: List[str] = allInputLines[0].split("\n")
   yourTicketInput: str = allInputLines[1].split("\n")[1].strip()
   nearbyTicketInput: List[str] = [s.strip() for s in allInputLines[2].split("\n")[1:]]

   fieldsList: List[Field] = constructFieldsList(fieldsInput)
   
   # Part 1
   print(f"Part 1 -- Error Rate: {calculateErrorRate(fieldsList, nearbyTicketInput)}")
   
   # Part 2
   relationships: List[str] = determineFieldTicketRelationships(fieldsList, nearbyTicketInput)
   whiteFlag(2, "Product of Departure Tickets", "12/16")

if __name__ == "__main__":
   main()

"""
--- Day 16: Ticket Translation ---
--- Part One ---
You collect the rules for ticket fields, the numbers on your ticket, and the numbers on other nearby
tickets for the same train service (via the airport security cameras) together into a single document
you can reference (your puzzle input).
The rules for ticket fields specify a list of fields that exist somewhere on the ticket and the valid
ranges of values for each field. For example, a rule like class: 1-3 or 5-7 means that one of the fields
in every ticket is named class and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3
and 5 are both valid in this field, but 4 is not).
Start by determining which tickets are completely invalid; these are tickets that contain values which
aren't valid for any field. Ignore your ticket for now.
It doesn't matter which position corresponds to which field; you can identify invalid nearby tickets
by considering only whether tickets contain values that are not valid for any field.
Consider the validity of the nearby tickets you scanned. What is your ticket scanning error rate?
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those tickets entirely. Use
the remaining valid tickets to determine which field is which.
Using the valid ranges for each field, determine what order the fields appear on the tickets. The order
is consistent between all tickets: if seat is the third field, it is the third field on every ticket,
including your ticket.
Once you work out which field is which, look for the six fields on your ticket that start with the word
departure. What do you get if you multiply those six values together?
"""