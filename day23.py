# 12/23/20

from Helpers.FileHelper import readFile
from typing import List, Set
FILEPATH: str = "Input/day23.txt"

class Cups:
   """
   Representing a game of cups
   """
   def __init__(self, cups: str):
      self.nums: List[int] = []
      for ch in cups:
         self.nums.append(int(ch))
   
   def getLength(self) -> int:
      """
      Expedites getting length of nums
      """
      return len(self.nums)
   
   def addNums(self, index: int, nums: List[int]) -> None:
      """
      Adds numbers to the specified index in the nums list
      """
      if index < 0 or index > self.getLength():
         raise Exception("Invalid insertion index in addNums()")
      
      for i in range(len(nums) - 1, -1, -1):
         self.nums.insert(index, nums[i])
   
   def move(self, roundNum: int, printAfterEachRound: bool) -> None:
      """
      Simulates moves for x rounds, and optionally prints config after each round
      """
      if roundNum <= 0:
         return
      
      currentIndex, currentNum = 0, 0
      destinationIndex, destinationNum = 0, 0
      numsSet: Set[int] = set(self.nums)
      pickedUpCups: List[int] = []
      first: bool = True
      
      for i in range(1, roundNum + 1, 1):
         if printAfterEachRound:
            print(f"After round {i} -- {self.nums} | ", end="")
         
         if not first:
            currentIndex = (self.nums.index(currentNum) + 1) % self.getLength()
         first = False
         currentNum = self.nums[currentIndex]
         pickedUpCups.clear()
         curNumsSet: Set[int] = numsSet.copy()

         for j in range(1, 4, 1):
            popIndex: int = (currentIndex + 1) % self.getLength()
            if currentIndex >= self.getLength():
               popIndex = 0

            temp: int = self.nums.pop(popIndex)
            curNumsSet.remove(temp)
            pickedUpCups.append(temp)
         
         destinationNum = currentNum - 1
         while destinationNum not in curNumsSet:
            destinationNum -= 1
            if destinationNum < min(curNumsSet):
               destinationNum = max(curNumsSet)
               break    
         
         destinationIndex = (self.nums.index(destinationNum) + 1) % self.getLength()
         self.addNums(destinationIndex, pickedUpCups)

         if printAfterEachRound:
            print(f"cur: {currentNum} | dest: {destinationNum} | picked up cups: {pickedUpCups}")

      if printAfterEachRound:
         print(f"Last: {self.nums}")
   
   def stringify(self, x: int) -> str:
      """
      Create a string from the specified number in the list to the end.
      If the number is not there, simply stringifies what is currently in the list.
      """
      s: str = ""
      index: int = 0
      try:
         index: int = self.nums.index(x)
      except:
         pass
      
      count: int = 0
      while count < self.getLength():
         s += str(self.nums[index])
         index = (index + 1) % self.getLength()
         count += 1

      return s

   def __repr__(self):
      return f"Cups game config: __{self.nums}__"

def main():
   inputLine: str = readFile(FILEPATH)[0]
   game: Cups = Cups(inputLine)
   
   # Part 1
   game.move(100, False)
   print(game.stringify(1)[1:])

   # Part 2

if __name__ == "__main__":
   main()

"""
--- Day 23: Crab Cups ---
--- Part One ---
The small crab challenges you to a game! The crab is going to mix up some cups, and you have to predict
where they'll end up. The cups will be arranged in a circle and labeled clockwise (your puzzle input).
For example, if your labeling were 32415, there would be five cups in the circle; going clockwise around
the circle from the first cup, the cups would be labeled 3, 2, 4, 1, 5, and then back to 3 again.
Before the crab starts, it will designate the first cup in your list as the current cup. The crab is
then going to do 100 moves.
Each move, the crab does the following actions:
    - The crab picks up the three cups that are immediately clockwise of the current cup. They are
      removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
    - The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
      If this would select one of the cups that was just picked up, the crab will keep subtracting one
      until it finds a cup that wasn't just picked up. If at any point in this process the value goes below
      the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
    - The crab places the cups it just picked up so that they are immediately clockwise of the destination
      cup. They keep the same order as when they were picked up.
    - The crab selects a new current cup: the cup which is immediately clockwise of the current cup.
Using your labeling, simulate 100 moves. What are the labels on the cups after cup 1?
--- Part Two ---
"""