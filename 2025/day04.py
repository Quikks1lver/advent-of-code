from PythonHelpers.ArrayHelpers import is_inbounds
from PythonHelpers.FileHelpers import read_2D_array
from PythonHelpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2025/Input/day04.txt"
   
PAPER = '@'
ACCESSIBLE_TILE = '.'

# Returns locations of accessible papers.
def solve(input: List[List[str]]) -> List[Tuple[int, int]]:
    accessible_papers: List[Tuple[int, int]] = []

    for row in range(len(input)):
        for col in range(len(input[0])):
            this_ch = input[row][col]

            if this_ch != PAPER:
                continue
            
            num_papers_adjacent = 0

            for row_move in range(-1, 2, 1):
                for col_move in range(-1, 2, 1):
                    if row_move == 0 and col_move == 0:
                        continue
                    
                    new_r, new_c = row_move + row, col_move + col
                    if is_inbounds(input, new_r, new_c) and input[new_r][new_c] == PAPER:
                        num_papers_adjacent += 1
            
            if num_papers_adjacent < 4:
                accessible_papers.append((row, col))

    return accessible_papers

def part1(input: List[List[str]]) -> int:
    return len(solve(input))

def part2(input: List[List[str]]) -> int:
    total = 0
    prev_iteration_total = None

    while prev_iteration_total != total:
        prev_iteration_total = total
        p1_ans = solve(input)
        total += len(p1_ans)
        for r, c in p1_ans:
            input[r][c] = ACCESSIBLE_TILE

    return total

def main() -> None:
    input: List[List[str]] = read_2D_array(FILEPATH, str)

    PART1(part1, input)
    PART2(part2, input)

if __name__ == "__main__": main()
