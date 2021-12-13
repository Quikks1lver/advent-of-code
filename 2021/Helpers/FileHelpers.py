from typing import List, Callable, Generic

def read_lines(filename: str) -> List[str]:
   """
   Returns a list of each line from given input file
   """
   with open(filename, "r") as file:
      return [line for line in file.readlines()]

def read_2D_array(filename: str, data_type: Callable) -> list:
   """
   Returns a 2-D array given from input file, converts elements into data type of choosing via
   input function
   """
   return [[data_type(c) for c in line.strip()] for line in read_lines(filename)]