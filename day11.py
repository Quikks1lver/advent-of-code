# 12/11/20

from Helpers.FileHelper import readFile
from typing import List, Tuple, Union
FILEPATH: str = "Input/day11.txt"

# constants
EMPTY: str = "L"
FLOOR: str = "."
OCCUPIED: str = "#"
DEBUGGING: bool = False

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
            if DEBUGGING:
               print(f"currently: {seats[row][col]} |  {change.row}, {change.col}, {change.newState}")
            return change
   
   if numOccupiedSeats == 0 and not occupied:
      change: SeatChange = SeatChange(row, col, OCCUPIED)
      if DEBUGGING:
         print(f"currently: {seats[row][col]} |  {change.row}, {change.col}, {change.newState}")
      return change

def main():
   seats: List[str] = [line.strip() for line in readFile(FILEPATH)]
   rowBound: int = len(seats)
   colBound: int = len(seats[0])
   changes: List[SeatChange] = []
   tempChange: Union[SeatChange, None] = None
   flag: bool = True
   numRounds: int = 0
   
   while flag:
      flag = False
      numRounds += 1
      newSeats = []
      for i in range(0, rowBound):
         newSeatLine = ""
         for j in range(0, colBound):
            tempChange = None
            tempChange = determineSeatChanges(seats, i, j, rowBound, colBound, 4)
            if tempChange != None:
               newSeatLine += tempChange.newState
               flag = True
            else:
               newSeatLine += seats[i][j]
         newSeats.append(newSeatLine)

      seats.clear()
      seats = newSeats

   if DEBUGGING:
      print(f"Numrounds til no change: {numRounds}")
   numSeats: int = 0
   for i in range(0, rowBound):
      for j in range(0, colBound):
         if seats[i][j] == OCCUPIED:
            numSeats += 1
   
   print(f"Part 1 -- Numseats: {numSeats}")

if __name__ == "__main__":
   main()

"""

--- Part One ---

--- Part Two ---
"""