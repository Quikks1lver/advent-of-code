from collections import deque
from PythonHelpers.ArrayHelpers import is_inbounds
from PythonHelpers.FileHelpers import read_2D_array
from PythonHelpers.PrintSolution import *
from typing import Deque, Dict, List, Set, Tuple
FILEPATH = "2025/Input/day07.txt"

START = 'S'
SPLITTER = '^'

def part1(input: List[List[str]], start: Tuple[int, int]) -> int:
    visited: Set[Tuple[int, int]] = set()
    
    # Dequeue from beginning and queue at end.
    queue: Deque[Tuple[int, int]] = deque()
    queue.append(start)

    split_count = 0

    while len(queue) > 0:
        dequeued_val = queue.popleft()
        next_step = (dequeued_val[0]+1, dequeued_val[1])
        
        if not is_inbounds(input, next_step[0], next_step[1]) or next_step in visited:
            continue

        if input[next_step[0]][next_step[1]] == SPLITTER:
            split_count += 1
            queue.append((next_step[0], next_step[1]-1))
            queue.append((next_step[0], next_step[1]+1))
        else:
            queue.append(next_step)
        
        visited.add(next_step)
    
    return split_count

def recurse(
        input: List[List[str]],
        memoized_map: Dict[Tuple[int, int], int],
        here: Tuple[int, int]
    ) -> int:
    memo_val = memoized_map.get(here)

    if memo_val is not None:
        return memo_val
    
    next_step = here[0]+1, here[1]
    if not is_inbounds(input, next_step[0], next_step[1]):
        return 1
    
    if input[next_step[0]][next_step[1]] == SPLITTER:
        memo_val = recurse(input, memoized_map, (next_step[0], next_step[1]-1)) \
            + recurse(input, memoized_map, (next_step[0], next_step[1]+1))
    else:
        memo_val = recurse(input, memoized_map, next_step)
    
    memoized_map[here] = memo_val
    return memo_val

def part2(input: List[List[str]], start: Tuple[int, int]) -> int:
    memoized_map: Dict[Tuple[int, int], int] = dict()
    recurse(input, memoized_map, start)
    return memoized_map[start]

def main() -> None:
    input: List[List[str]] = read_2D_array(FILEPATH, str)
    start: Tuple[int, int] = (0, 0)
    
    for col in range(len(input[0])):
        if input[0][col] == START:
            start = (0, col)
            break

    PART1(part1, input, start)
    PART1(part2, input, start)

if __name__ == "__main__": main()
