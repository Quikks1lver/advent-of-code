from typing import List

def read_lines(filename: str) -> List[str]:
   """
   Returns a list of each line from given input file
   """
   with open(filename, "r") as file:
      return [line for line in file.readlines()]