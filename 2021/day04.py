from Helpers.FileHelpers import read_lines
from typing import List, Set
FILEPATH = "2021/Input/day04.txt"

class BingoBoard():
   def __init__(self, board_lines: List[List[str]]):
      self.horiz_sets: List[Set[int]] = [set() for i in range(5)] 
      self.vert_sets: List[Set[int]] = [set() for i in range(5)]
      self.won: bool = False

      for row in range(len(board_lines)):
         for col in range(len(board_lines[row])):
            ch = int(board_lines[row][col])
            self.horiz_sets[row].add(ch)
            self.vert_sets[col].add(ch)

   def mark_board(self, num: int) -> None:
      won = False
      
      for h in self.horiz_sets:
         if num in h:
            h.remove(num)
            if len(h) == 0:
               won = True
      
      for v in self.vert_sets:
         if num in v:
            v.remove(num)
            if len(v) == 0:
               won = True

      if won == True:
         self.won = won

   def calculate_score(self, num_just_called: int) -> int:
      score = 0

      for h in self.horiz_sets:
         for val in h:
            score += val

      return score * num_just_called

   def has_won(self) -> bool:
      return self.won

   @staticmethod
   def create_bingo_boards_list(bingo_input: List[str]):
      return [BingoBoard(bingo_input[i : i + 5]) for i in range(0, len(bingo_input), 6)]

def find_first_bingo_winner(bingo_boards: List[BingoBoard], nums: List[int]) -> int:
   for i in nums:
      for b in bingo_boards:
            b.mark_board(i)
            
            if b.has_won():
               return b.calculate_score(i)

def find_last_bingo_winner(bingo_boards: List[BingoBoard], nums: List[int]) -> int:
   winner_count = 0
   
   for i in nums:
      for b in bingo_boards:
            if not b.has_won():
               b.mark_board(i)

               if b.has_won():
                  winner_count += 1
               
               if winner_count == len(bingo_boards):
                  return b.calculate_score(i)

def main():
   input_lines: List[str] = [line.strip() for line in read_lines(FILEPATH)]
   bingo_input: List[str] = [line.split() for line in input_lines[2:]]
   nums_to_be_called = [int(i) for i in input_lines[0].split(",")]

   print(f"Part 1 -- {find_first_bingo_winner(BingoBoard.create_bingo_boards_list(bingo_input), nums_to_be_called)}")
   print(f"Part 2 -- {find_last_bingo_winner(BingoBoard.create_bingo_boards_list(bingo_input), nums_to_be_called)}")

if __name__ == "__main__":
   main()