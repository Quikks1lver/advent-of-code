from Helpers.FileHelpers import read_lines
from Helpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2023/Input/day01.txt"

def part1(input: List[str]) -> int:
   total = 0

   for line in input:
      firstCh = ""
      lastCh = ""
      
      for ch in line:
         if ch.isdigit():
            if firstCh == "":
               firstCh = ch
            lastCh = ch

      total += int(firstCh + lastCh)
   
   return total

def part2(input: List[str]) -> int:
   replaceVals = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
   total = 0

   for lineIndex, line in enumerate(input):
      firstChars: List[Tuple[int, int]] = []
      lastChars: List[Tuple[int, int]] = []
      
      for index, val in enumerate(replaceVals):   
         newLine = line.replace(val, str("".join(["_" for _ in range(len(val) - 1)])) + str(index + 1))

         firstCh = True
         for indexCh, ch in enumerate(newLine):
            if ch.isdigit():
               
               if firstCh:
                  firstChars.append((indexCh, int(ch)))
                  firstCh = False
               
               lastChars.append((indexCh, int(ch)))
      
      firstChars.sort(key=lambda item: item[0])
      lastChars.sort(key=lambda item: item[0], reverse=True)

      total += (firstChars[0][1] * 10 + lastChars[0][1])
   
   return total

def main():
   input: List[str] = [line.strip() for line in read_lines(FILEPATH)]
   
   PART1(part1, input)
   PART2(part2, input)

if __name__ == "__main__": main()