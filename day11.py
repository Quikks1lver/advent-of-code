# 12/11/20

from Helpers.FileHelper import readFile
from typing import List, Tuple, Union
FILEPATH: str = "Input/day11.txt"

# constants
EMPTY: str = "L"
FLOOR: str = "."
OCCUPIED: str = "#"

class SeatChange:
   """
   Represents a changed seat
   """
   def __init__(self, row: int, col: int, newState: str):
      self.row = row
      self.col = col
      self.newState = newState

def mutateElement(dArray: List[str], row: int, col: int, newStr: str) -> None:
   """
   Changes the given index's contents to newStr
   """
   dArray[row][col] = newStr

def isOutOfBounds(row: int, col: int, rowBound: int, colBound: int) -> bool:
   """
   Checks if a row and col are out of bounds for a double array
   """
   if row < 0 or row >= rowBound or col < 0 or col >= colBound:
      return True
   return False

def determineSeatChanges(seats: List[str], row: int, col: int, rowBound: int, colBound: int, changeTolerance: int) -> (Union[None, SeatChange]):
   """
   Changes seat's state in place, returns a SeatChange object if necessary
   """
   occupied: bool = True if seats[row][col] == OCCUPIED else False
   numOccupiedSeats: int = 0
   tempRow, tempCol = 0, 0

   if seats[row][col] == FLOOR:
      return None
   
   states: Tuple[Tuple[int]] = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

   for state in states:
      tempRow, tempCol = state[0] + row, state[1] + col
      if not isOutOfBounds(tempRow, tempCol, rowBound, colBound):
         if seats[tempRow][tempCol] == OCCUPIED:
            numOccupiedSeats += 1
         if occupied and numOccupiedSeats >= changeTolerance:
            change: SeatChange = SeatChange(row, col, EMPTY)
            return change
   
   if numOccupiedSeats == 0 and not occupied:
      change: SeatChange = SeatChange(row, col, OCCUPIED)
      return change
   else:
      return None

# A wacky function name, I know. Tis for fun =)
def determineSeatChangesAsFarAsTheEyeCanSee(seats: List[str], row: int, col: int, rowBound: int, colBound: int, changeTolerance: int) -> (Union[None, SeatChange]):
   """
   Changes seat's state in place, with more enhanced rules, returns a SeatChange object if necessary
   """
   occupied: bool = True if seats[row][col] == OCCUPIED else False
   numOccupiedSeats: int = 0
   tempRow, tempCol = 0, 0

   if seats[row][col] == FLOOR:
      return None
   
   states: Tuple[Tuple[int]] = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

   for state in states:
      tempRow, tempCol = state[0] + row, state[1] + col
      firstFlag = True

      while not isOutOfBounds(tempRow, tempCol, rowBound, colBound):
         if not firstFlag:
            tempRow, tempCol = tempRow + state[0], tempCol + state[1]
         firstFlag = False

         if isOutOfBounds(tempRow, tempCol, rowBound, colBound):
            break
         if seats[tempRow][tempCol] == EMPTY:
            break
         if seats[tempRow][tempCol] == OCCUPIED:
            numOccupiedSeats += 1
            break
      
   if occupied and numOccupiedSeats >= changeTolerance:
      change: SeatChange = SeatChange(row, col, EMPTY)
      return change
   elif numOccupiedSeats == 0 and not occupied:
      change: SeatChange = SeatChange(row, col, OCCUPIED)
      return change
   else:
      return None

def countOccupiedSeats(seats: List[str], rowBound, colBound) -> int:
   """
   Counts number of occupied seats
   """
   numSeats: int = 0
   for i in range(0, rowBound):
      for j in range(0, colBound):
         if seats[i][j] == OCCUPIED:
            numSeats += 1
   return numSeats

def runUntilNoChange(seats: List[str], threshold: int, asFarAsTheEyeCanSee: bool) -> int:
   """
   Runs seat changing algorithm until equilibrium
   """
   flag: bool = True
   tempChange: Union[SeatChange, None] = None
   rowBound: int = len(seats)
   colBound: int = len(seats[0])

   seats = seats.copy()

   while flag:
      flag = False
      newSeats = []
      for i in range(0, rowBound):
         newSeatLine = ""
         for j in range(0, colBound):
            tempChange = None
            
            if asFarAsTheEyeCanSee:
               tempChange = determineSeatChangesAsFarAsTheEyeCanSee(seats, i, j, rowBound, colBound, threshold)
            else:
               tempChange = determineSeatChanges(seats, i, j, rowBound, colBound, threshold)
            
            if tempChange != None:
               newSeatLine += tempChange.newState
               flag = True
            else:
               newSeatLine += seats[i][j]
         newSeats.append(newSeatLine)

      seats.clear()
      seats = newSeats
   
   return countOccupiedSeats(seats, rowBound, colBound)

def main():
   seats: List[str] = [line.strip() for line in readFile(FILEPATH)]
   
   # Part 1
   print(f"Part 1 -- Numseats: {runUntilNoChange(seats, 4, False)}")
   
   # Part 2
   print(f"Part 2 -- Numseats: {runUntilNoChange(seats, 5, True)}")

if __name__ == "__main__":
   main()

"""
--- Day 11: Seating System ---
--- Part One ---
By modeling the process people use to choose (or abandon) their seat in the waiting area, you're
pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).
The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an
occupied seat (#). For example, the initial seat layout might look like this ... (ex).
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
Simulate your seating area by applying the seating rules repeatedly until no seats change state.
How many seats end up occupied?
--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent
seats - they care about the first seat they can see in each of those eight directions!
Now, instead of considering just the eight immediately adjacent seats, consider the first seat in
each of those eight directions. For example, the empty seat below would see eight occupied seats:
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied
seats for an occupied seat to become empty.
Given the new visibility method and the rule change for occupied seats becoming empty, once
equilibrium is reached, how many seats end up occupied?
"""