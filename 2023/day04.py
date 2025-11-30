from Helpers.FileHelpers import read_lines
from Helpers.PrintSolution import *
from typing import List, Tuple, Set
import re
FILEPATH = "2023/Input/day04.txt"

INPUT_REGEX = re.compile("(\d+\s*)")

def parseInput(input: List[str]) -> List[Tuple[Set[int], Set[int]]]:
   output: List[Tuple[Set[int], Set[int]]] = list()
   
   for line in input:
      firstSubString, secondSubString = line.split("|")
      winningNums = [int(_) for _ in INPUT_REGEX.findall(firstSubString)]
      winningNums.pop(0) # remove card number
      numbersYouHave = [int(_) for _ in INPUT_REGEX.findall(secondSubString)]
      output.append((set(winningNums), set(numbersYouHave)))

   return output

def part1(input: List[Tuple[Set[int], Set[int]]]) -> int:
   return sum([int(2 ** (len(winningNums.intersection(numbersYouHave)) - 1)) for winningNums, numbersYouHave in input])

def part2(input: List[Tuple[Set[int], Set[int]]]) -> int:
   numCards = [1 for _ in range(len(input))]

   for index, (winningNums, numbersYouHave) in enumerate(input):
      addedCards = len(winningNums.intersection(numbersYouHave))
      multiplier = numCards[index]

      for i in range(index + 1, index + addedCards + 1, 1):
         numCards[i] += multiplier
    
   return sum(numCards)

def main():
   rawInput: List[str] = [line.strip() for line in read_lines(FILEPATH)]
   input = parseInput(rawInput)

   PART1(part1, input)
   PART2(part2, input)

if __name__ == "__main__": main()