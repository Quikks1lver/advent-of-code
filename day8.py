# 12/8/20

from Helpers.FileHelper import readFile
from typing import List, Set
from enum import Enum
FILEPATH: str = "Input/day8.txt"

class Type(Enum):
   """
   Defines an action type (enum)
   """
   ACC = "acc"
   JMP = "jmp"
   NOP = "nop"

class Action:
   """
   Represents an action from the input
   """
   def __init__(self, type: Type, payload: int):
      self.type: Type = type
      self.payload = payload      

def tokenizeAction(s: str) -> Action:
   """
   Tokenizes input string into an Action type
   """
   s = s.strip()
   
   tokenType: Type = None
   tokenParam: int = 0

   optParam: int = 0
   actionType: str = s[0:3]
   actionParam: int = s[4:]

   if actionType == "acc":
      tokenType = Type.ACC
      tokenParam = int(actionParam)
   elif actionType == "jmp":
      tokenType = Type.JMP
      tokenParam = int(actionParam)
   else:
      tokenType = Type.NOP

   return Action(tokenType, tokenParam)

def parseInstructions(instructions: List[str]) -> (int, bool):
   """
   Parses a list of game instructions, and returns global
   accumulator right before an infinite loop arises. Also returns
   1 if reached end of the file, 0 otherwise.
   """
   visitedInstructions: Set[int] = set()
   globalAcc: int = 0
   curAction: Action = None
   curLine: int = 0
   instructionsLen = len(instructions)
   REACHED_END: bool = False

   while curLine < instructionsLen:
      if curLine in visitedInstructions:
         return globalAcc, REACHED_END
      visitedInstructions.add(curLine)
      
      curAction = tokenizeAction(instructions[curLine])

      if curAction.type == Type.ACC:
         globalAcc += curAction.payload
         curLine += 1
      elif curAction.type == Type.JMP:
         curLine += curAction.payload
      else: # nop
         curLine += 1
   
   REACHED_END = True
   return globalAcc, REACHED_END

def fixGame(instructions: List[str]) -> int:
   """
   Fixes the game by changing nop <=> jmp 1 time, and outputs acc. after
   changing this one line (returns final val of acc. when the game is fixed).
   """
   newInstructions: List[str] = instructions.copy()
   instructionsLen: int = len(newInstructions)
   curLine: int = 0
   curAction: Action = None

   endgameAcc: int = 0
   endFlag: bool = False

   JMP: str = "jmp"
   NOP: str = "nop"

   while curLine < instructionsLen:
      curAction = tokenizeAction(newInstructions[curLine])

      if curAction.type == Type.ACC:
         curLine += 1
      elif curAction.type == Type.JMP:
         newInstructions[curLine] = newInstructions[curLine].replace(JMP, NOP)
         endgameAcc, endFlag = parseInstructions(newInstructions)
         if endFlag:
            return endgameAcc
         newInstructions[curLine] = newInstructions[curLine].replace(NOP, JMP)
         curLine += curAction.payload
      else: # nop
         newInstructions[curLine] = newInstructions[curLine].replace(NOP, JMP)
         endgameAcc, endFlag = parseInstructions(newInstructions)
         if endFlag:
            return endgameAcc
         newInstructions[curLine] = newInstructions[curLine].replace(JMP, NOP)
         curLine += 1

def main():
   instructions: List[str] = readFile(FILEPATH)

   # Part 1
   acc, reached_end = parseInstructions(instructions)
   print(f"Part 1 -- global acc: {acc}")

   # Part 2
   acc = fixGame(instructions)
   print(f"Part 2 -- global acc, after fixing game: {acc}")

if __name__ == "__main__":
   main()

"""
--- Day 8: Handheld Halting ---
--- Part One ---
Your flight to the major airline hub reaches cruising altitude without incident. While you consider
checking the in-flight menu for one of those drinks that come with a little umbrella, you are interrupted
by the kid sitting next to you.
Their handheld game console won't turn on! They ask if you can take a look.
The boot code is represented as a text file with one instruction per line of text. Each instruction
consists of an operation (acc, jmp, or nop) and an argument (a signed number like +4 or -20).
This is an infinite loop: with this sequence of jumps, the program will run forever. The moment the
program tries to run any instruction a second time, you know it will never terminate.
Immediately before the program would run an instruction a second time, the value in the accumulator is 5.
Run your copy of the boot code. Immediately before any instruction is executed a second time,
what value is in the accumulator?
--- Part Two ---
After some careful analysis, you believe that exactly one instruction is corrupted.
Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp).
What is the value of the accumulator after the program terminates?
"""