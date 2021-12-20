from enum import Enum
from Helpers.FileHelpers import read_lines
from typing import List, Set, Tuple
FILEPATH = "2021/Input/day13.txt"

class FoldInstruction():
   FOLD_INSTRUCTION_INDICATOR_STR = "fold along"
   
   class Axis(Enum):
      X = "x"
      Y = "y"
   
   def __init__(self, s: str) -> None:
      instruction = s.split()[2].split("=")
      self.axis = FoldInstruction.Axis.X if instruction[0] == "x" else FoldInstruction.Axis.Y
      self.value = int(instruction[1])

def parse_input(input_lines: List[str]) -> Tuple[Set[Tuple[int, int]], List[FoldInstruction]]:
   dots: Set[Tuple[int, int]] = set()
   fold_instructions: List[FoldInstruction] = list()

   for s in input_lines:
      if FoldInstruction.FOLD_INSTRUCTION_INDICATOR_STR in s:
         fold_instructions.append(FoldInstruction(s))
      else:
         dot_input = s.split(",")
         if len(s) == 0: # blank line
            continue
         dots.add((int(dot_input[0]), int(dot_input[1])))
   
   return dots, fold_instructions

def fold_origami(dots: Set[Tuple[int, int]], fold_instructions: List[FoldInstruction]) -> Set[Tuple[int, int]]:
   output_dots: Set[Tuple[int, int]] = dots.copy()

   for instruction in fold_instructions:
      temp_dots = output_dots.copy()
      
      for x, y in output_dots:
         if instruction.axis == FoldInstruction.Axis.X:
            if x > instruction.value:
               new_x = instruction.value - (x - instruction.value)
               temp_dots.add((new_x, y))
               temp_dots.remove((x, y))
         else:
            if y > instruction.value:
               new_y =  instruction.value - (y - instruction.value)
               temp_dots.add((x, new_y))
               temp_dots.remove((x, y))

      output_dots = temp_dots

   return output_dots

def print_origami_code(folded_origami: Set[Tuple[int, int]]) -> None:
   maxX = max([x for x, y in folded_origami]) + 1
   maxY = max([y for x, y in folded_origami]) + 1

   output = [[" " for x in range(maxX)] for y in range(maxY)]
   for x, y in folded_origami:
      output[y][x] = "#"

   for row in output:
      print("".join(row))

def main():
   dots, fold_instructions = parse_input([line.strip() for line in read_lines(FILEPATH)])
   
   print(f"Part 1 -- {len(fold_origami(dots, fold_instructions[0:1]))}")
   print("Part 2 -- BLHFJPJF")
   print_origami_code(fold_origami(dots, fold_instructions))

if __name__ == "__main__":
   main()