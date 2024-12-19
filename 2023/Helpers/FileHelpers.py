from typing import Callable, List

def read_lines(filename: str) -> List[str]:
   """
   Returns a list of each line from given input file
   """
   with open(filename, "r") as file:
      return file.readlines()
   
def read_2D_array(filename: str, data_type: Callable) -> List[List]:
   """
   Returns a 2-D array given from input file, converts elements into data type of choosing via
   input function
   """
   return [[data_type(c) for c in line.strip()] for line in read_lines(filename)]

def read_file(filename: str) -> List[str]:
   """
   Reads a file and returns a list of the data
   """
   try:
      with open(filename, "r") as fp:
         return fp.readlines()
   except:
      raise Exception(f"Failed to open {filename}")

def read_file_with_line_breaks(filepath: str) -> List[str]:
   """
   Reads an input file, data separated by fully blank lines, and outputs a list of lists of the data
   """
   input: List[str] = [line.strip() for line in read_file(filepath)]

   output: List[List[str]] = []
   temp_list: List[str] = []
   
   for line in input:
      if line == '':
         output.append(temp_list)
         temp_list = []
      else:
         temp_list.append(line)
   output.append(temp_list) # last one

   return output