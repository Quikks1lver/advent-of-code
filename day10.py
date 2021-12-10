from Helpers.FileHelpers import read_lines
from typing import List, Dict, Tuple
FILEPATH = "Input/day10.txt"

COMPLETION_LOOKUP_TABLE: Dict[str, int] = {")": 1, "]": 2, "}": 3, ">": 4}
ILLEGAL_LOOKUP_TABLE: Dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
CLOSING_CHARS_DICT: Dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}
OPENING_CHARS_DICT: Dict[str, str] = {"(": ")", "[": "]", "{": "}", "<": ">"}

def calculate_syntax_error_score(input_lines: List[str]) -> Tuple[int, List[str]]:
   total = 0
   stack = list()
   incomplete_lines: List[str] = list()

   for line in input_lines:
      is_incomplete_line: bool = True

      for ch in line:
         if ch in CLOSING_CHARS_DICT.keys():
            popped_char = stack.pop()
            if popped_char != CLOSING_CHARS_DICT[ch]:
               total += ILLEGAL_LOOKUP_TABLE[ch]
               is_incomplete_line = False
         else:
            stack.append(ch)
   
      if is_incomplete_line:
         incomplete_lines.append(line)

   return (total, incomplete_lines)

def calculate_middle_completion_score(incomplete_lines: List[str]) -> int:
   scores_list = list()
   stack = list()
   
   for line in incomplete_lines:
      for ch in line:
         if ch in CLOSING_CHARS_DICT.keys():
            stack.pop()
         else:
            stack.append(ch)

      score = 0
      stack.reverse()
      
      for element in stack:
         score *= 5
         score += COMPLETION_LOOKUP_TABLE[OPENING_CHARS_DICT[element]]
      
      scores_list.append(score)
      stack.clear()

   scores_list.sort()
   return scores_list[(int)(len(scores_list) / 2)]

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]

   syntax_error_score, incomplete_lines = calculate_syntax_error_score(input_lines)
   print(f"Part 1 -- {syntax_error_score}")
   print(f"Part 2 -- {calculate_middle_completion_score(incomplete_lines)}")

if __name__ == "__main__":
   main()