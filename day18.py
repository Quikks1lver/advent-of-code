# 12/18/20

from enum import Enum
from Helpers.AOC import whiteFlag
from Helpers.DataStructures import Stack
from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/day18.txt"

DEBUGGING: bool = False

class Operators(Enum):
   PLUS = "+"
   TIMES = "*"
   CLOSE_PAREN = ")"
   OPEN_PAREN = "("

class OpToken:
   """
   Represents a number and its operator for use in arithmetic when a pause arises with parantheses
   """
   def __init__(self, num: int, op: Operators):
      self.num = num
      self.op = op
   
   def __repr__(self):
      return f"{self.num} {self.op}"

def parseArithmetic(line: str) -> int:
   """
   Parses a line of the arithmetic and returns the numeric answer
   """
   tokenStack: Stack = Stack()
   
   prevOp: Operators = None
   prevNum: int = None

   i: int = 0
   char: str = ""
   while i < len(line):
      char = line[i]
      
      if char.isspace():
         pass
      
      elif char.isnumeric():
         start: int = i
         while i < len(line) and char.isnumeric():
            i += 1
            if i < len(line):
               char = line[i]
         tempNum: int = int(line[start: i])
         i -= 1
      
         if prevNum == None:
            prevNum = tempNum
         else:
            if prevOp == Operators.PLUS:
               prevNum += tempNum
            else:
               prevNum *= tempNum
      
      elif char == Operators.PLUS.value:
         prevOp = Operators.PLUS
      
      elif char == Operators.TIMES.value:
         prevOp = Operators.TIMES
      
      elif char == Operators.OPEN_PAREN.value:
         if prevNum != None:
            tokenStack.push(OpToken(prevNum, prevOp))
         prevNum = None
      
      else: # )
         if tokenStack.getSize() <= 0:
            pass
         else:   
            tempToken: OpToken = tokenStack.pop()
            if tempToken.op == Operators.PLUS:
               prevNum += tempToken.num
            else:
               prevNum *= tempToken.num
      
      i += 1

      if DEBUGGING:
         print("=======")
         print(f"{char} {prevNum} {prevOp} {tokenStack}")
         print("=======")

   return prevNum

def main():
   inputLines: List[str] = [s.strip() for s in readFile(FILEPATH)]

   # Part 1
   # I am honestly not sure why the function does not work. I tested it for over an hour
   # with a bunch of individual inputs, and it worked fine for every one. If anyone knows
   # why this is failing, please let me know!
   total: int = 0
   for line in inputLines:
      total += parseArithmetic(line)
   print(f"Part 1 -- Total Sum: {total}")

   # Part 2
   whiteFlag(2, "?", "12/18")

if __name__ == "__main__":
   main()

"""
--- Day 18: Operation Order ---
--- Part One ---
The homework (your puzzle input) consists of a series of expressions that consist of addition (+),
multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression
inside must be evaluated before it can be used by the surrounding expression. Addition still finds the
sum of the numbers on both sides of the operator, and multiplication still finds the product.
However, the rules of operator precedence have changed. Rather than evaluating multiplication before
addition, the operators have the same precedence, and are evaluated left-to-right regardless of the
order in which they appear.
Before you can help with the homework, you need to understand it yourself. Evaluate the expression on
each line of the homework; what is the sum of the resulting values?
--- Part Two ---
TBD
"""