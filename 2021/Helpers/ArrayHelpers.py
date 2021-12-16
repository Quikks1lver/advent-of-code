from typing import List

def is_inbounds(twod_array: List[list], row: int, col: int) -> bool:
   """
   Returns true if the row and column indices are within the bounds of the array, false otherwise
   """
   return True if row >= 0 and row < len(twod_array) and col >= 0 and col < len(twod_array[0]) else False