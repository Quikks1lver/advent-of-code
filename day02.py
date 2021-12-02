from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "Input/day02.txt"

class Token():
   def __init__(self, string: str):
      temp = string.split(" ")
      self.val = temp[0]
      self.payload = int(temp[1])

   def __repr__(self):
      return f"{self.val} : {self.payload}"

def calculate_product(token_list: List[Token]) -> int:
   horiz, depth = 0, 0
   
   for token in token_list:
      if token.val == "forward":
         horiz += token.payload
      elif token.val == "down":
         depth += token.payload
      elif token.val == "up":
         depth -= token.payload
   
   return horiz * depth

def calculate_aim_product(token_list: List[Token]) -> int:
   horiz, depth = 0, 0
   aim = 0

   for token in token_list:
      if token.val == "down":
         aim += token.payload
      elif token.val == "up":
         aim -= token.payload
      elif token.val == "forward":
         horiz += token.payload
         depth += aim * token.payload

   return horiz * depth

def main():
   input_tokens = [Token(line.strip()) for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {calculate_product(input_tokens)}")
   print(f"Part 2 -- {calculate_aim_product(input_tokens)}")

if __name__ == "__main__":
   main()