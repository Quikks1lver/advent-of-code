# File readers for use elsewhere

from typing import List

def readFile(filename: str) -> List[str]:
   """
   Reads a file and returns a list of the data
   """
   
   try:
      with open(filename, "r") as fp:
         return fp.readlines()
   except:
      raise Exception(f"Failed to open {filename}")

def readFileWithEmptyLineBreaks(filepath: str) -> List[str]:
   """
   Reads an input file, data separated by fully blank lines, and outputs a list of the data
   """
   inputLines: List[str] = readFile(filepath)
   outputList: List[str] = []

   tempLine: str = ""
   for line in inputLines:
      if line == "\n":
         if tempLine != "":
            tempLine = tempLine.strip()
            outputList.append(tempLine)
         tempLine = ""
      else:
         tempLine += " " + line
   outputList.append(tempLine.strip()) # don't forget last one!

   return outputList