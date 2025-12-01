from typing import List

def read_lines(filename: str) -> List[str]:
   """
   Reads a file and returns a list of the data, stripped
   """
   try:
      with open(filename, "r") as fp:
         return [l.strip() for l in fp.readlines()]
   except:
      raise Exception(f"Failed to open {filename}")
