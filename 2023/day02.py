from Helpers.FileHelpers import read_lines
from typing import List
import re
FILEPATH = "2023/Input/day02.txt"

RED_REGEX = re.compile("(\d+) red")
GREEN_REGEX = re.compile("(\d+) green")
BLUE_REGEX = re.compile("(\d+) blue")

def part1(input: List[str]) -> int:
   RED_LIMIT = 12
   GREEN_LIMIT = 13
   BLUE_LIMIT = 14

   total = 0
   for index, line in enumerate(input):
      continueOn = False

      for match in RED_REGEX.findall(line):
         if int(match) > RED_LIMIT:
            continueOn = True
            break
      if continueOn:
         continue
         
      for match in GREEN_REGEX.findall(line):
         if int(match) > GREEN_LIMIT:
            continueOn = True
            break
      if continueOn:
         continue
         
      for match in BLUE_REGEX.findall(line):
         if int(match) > BLUE_LIMIT:
            continueOn = True
            break
      if continueOn:
         continue
    
      total += (index + 1)
   
   return total

def part2(input: List[str]) -> int:
   total = 0

   for index, line in enumerate(input):
      redLargest = 1
      greenLargest = 1
      blueLargest = 1

      for match in RED_REGEX.findall(line):
         if int(match) > redLargest:
            redLargest = int(match)

      for match in GREEN_REGEX.findall(line):
         if int(match) > greenLargest:
            greenLargest = int(match)
         
      for match in BLUE_REGEX.findall(line):
         if int(match) > blueLargest:
            blueLargest = int(match)        
    
      total += (redLargest * greenLargest * blueLargest)
   
   return total

def main():
   input: List[str] = [line.strip() for line in read_lines(FILEPATH)]
   print(f"Part 1 -- {part1(input)}")
   print(f"Part 2 -- {part2(input)}")

if __name__ == "__main__": main()