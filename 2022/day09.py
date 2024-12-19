from Helpers.FileHelpers import read_lines
from typing import List, Set, Tuple, Union
FILEPATH = "2022/Input/day09.txt"
         
def count_tail_visits(input: List[Tuple[str, int]], num_knots: int) -> int:
   def get_change_in_row_col(direction: str) -> Tuple[int, int]:
      match direction:
         case 'L': return (0, -1)
         case 'R': return (0, 1)
         case 'U': return (1, 0)
         case 'D': return (-1, 0)

   def calculate_move_for_2_units_away(head: Tuple[int, int], tail: Tuple[int, int]) -> Union[Tuple[int, int], None]:
      for change in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
         if add_knots(tail, change) == head:
            return (change[0] // 2, change[1] // 2)
      return None

   def calculate_move_for_diagonal(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
      return (1 if head[0] > tail[0] else -1, 1 if head[1] > tail[1] else -1)

   def is_touching(head: Tuple[int, int], tail: Tuple[int, int]) -> bool:
      for d_row in [-1, 0, 1]:
         for d_col in [-1, 0, 1]:
            if add_knots(head, (d_row, d_col)) == tail:
               return True
      return False
   
   add_knots = lambda x, y: (x[0] + y[0], x[1] + y[1])
   
   knots: List[Tuple[int, int]] = [(0, 0) for _ in range(num_knots)]
   visited: Set[Tuple[int, int]] = set()
   visited.add(knots[-1])

   for direction, magnitude in input:
      d_row, d_col = get_change_in_row_col(direction)
      
      for _ in range(magnitude):
         for i in range(len(knots) - 1):
            if i == 0:  # head always moves
               knots[i] = add_knots(knots[i], (d_row, d_col))

            if is_touching(knots[i], knots[i+1]):
               continue

            change_in_next_knot_for_2_units_away = calculate_move_for_2_units_away(knots[i], knots[i+1])
            if change_in_next_knot_for_2_units_away != None:
               knots[i+1] = add_knots(knots[i+1], change_in_next_knot_for_2_units_away)
            else:
               knots[i+1] = add_knots(knots[i+1], calculate_move_for_diagonal(knots[i], knots[i+1]))
            
            if i == len(knots) - 2: # keep track of last knot
               visited.add(knots[i+1])
   
   return len(visited)

def main():
   input: List[Tuple[str, int]] = [(dir, int(mag)) for dir, mag in [line.strip().split() for line in read_lines(FILEPATH)]]
   for i, num_knots in enumerate([2, 10]):
      print(f"Part {i+1} -- {count_tail_visits(input, num_knots)}")

if __name__ == "__main__": main()