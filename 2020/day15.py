# 12/15/20

from Helpers.FileHelper import readOneLineFileWithCommas
from typing import Dict, List, Set
FILEPATH: str = "2020/Input/day15.txt"

class MemoryGame:
   """
   Represents the elves's memory game
   """
   def __init__(self, startingNums: List[int]):
      self.startingNums: List[int] = startingNums
      self.prevNum: int = 0
      self.numToRoundMap: Dict[int, int] = dict()
   
   def findNthNum(self, endingRound: int) -> int:
      """
      Plays the memory game, stopping on the ending round and returning the number spoken
      """
      if endingRound <= 0:
         print("Invalid round number.")
         return None
      if endingRound <= len(self.startingNums):
         return self.startingNums[endingRound - 1]

      roundNum: int = 1
      firstTime: bool = False
      self.numToRoundMap = dict()

      for x in self.startingNums:
         self.numToRoundMap[x] = roundNum
         self.prevNum = x
         roundNum += 1
      
      firstTime = True
      while roundNum <= endingRound:
         # first time a number has been spoken
         if firstTime:
            self.numToRoundMap[self.prevNum] = roundNum - 1
            firstTime = False
            self.prevNum = 0
         # number is a previously spoken one
         else:
            diff: int = (roundNum - 1) - self.numToRoundMap[self.prevNum]
            self.numToRoundMap[self.prevNum] = roundNum - 1
            self.prevNum = diff
            
            if self.prevNum not in self.numToRoundMap:
               firstTime = True

         roundNum += 1

      return self.prevNum

def main():
   nums: List[int] = [int(s) for s in readOneLineFileWithCommas(FILEPATH)]
   game: MemoryGame = MemoryGame(nums)
   
   # Part 1
   print(f"Part 1 -- Number at round 2020: {game.findNthNum(2020)}")
   
   # Part 2 (takes ~10 s to run)
   print(f"Part 2 -- Number at round 30,000,000: {game.findNthNum(30000000)}")

if __name__ == "__main__":
   main()

"""
--- Day 15: Rambunctious Recitation ---
--- Part One ---
While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're
playing a memory game and are ever so excited to explain the rules!
In this game, the players take turns saying numbers. They begin by taking turns reading from a list
of starting numbers (your puzzle input). Then, each turn consists of considering the most recently
spoken number:
   - If that was the first time the number has been spoken, the current player says 0.
   - Otherwise, the number had been spoken before; the current player announces how many turns apart
     the number is from when it was previously spoken.
Given your starting numbers, what will be the 2020th number spoken?
--- Part Two ---
Impressed, the Elves issue you a challenge: determine the 30000000th number spoken.
Given your starting numbers, what will be the 30000000th number spoken?
"""