from typing import Any, Callable, List

def read_lines(filename: str) -> List[str]:
   """
   Reads a file and returns a list of the data, stripped
   """
   try:
      with open(filename, "r") as fp:
         return [l.strip() for l in fp.readlines()]
   except:
      raise Exception(f"Failed to open {filename}")

def read_2D_array(filename: str, data_type: Callable[..., Any]) -> List[List[Any]]:
   """
   Returns a 2-D array given from input file, converts elements into data type of choosing via
   input function
   """
   return [[data_type(c) for c in line.strip()] for line in read_lines(filename)]