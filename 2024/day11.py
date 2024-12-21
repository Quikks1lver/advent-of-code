# OK, this time we NEED big numbers! My C++ solution was overflowing even with 128-bit ints.

from PythonHelpers.FileHelpers import read_file
from PythonHelpers.PrintSolution import PART1, PART2
from collections import defaultdict
from typing import DefaultDict, List
FILEPATH = "2024/Input/day11.txt"

# I initially had this function using a list but it QUICKLY blew up for part 2.
# I consulted subreddit for some ideas as I was stuck. The key idea is we don't actually care about
# ordering, contrary to what problem says. Just keep track of frequencies using a dictionary.

def blink(initial_stones: List[int], num_blinks: int) -> int:
    # stone/number : frequency
    curr_stones: DefaultDict[int, int] = defaultdict(int)
    
    for stone in initial_stones:
        curr_stones[stone] += 1

    for _ in range(num_blinks):
        next_stones: DefaultDict[int, int] = defaultdict(int)
        next_stones.clear()

        for key, val in curr_stones.items():
            # 1. Replace 0 with 1.
            if key == 0:
                next_stones[1] += val
                continue
                
            # 2. Replace number with two halves if even # of digits.
            stringifiedNum: str = str(key)
            if len(stringifiedNum) % 2 == 0:
                halfwayPt: int = len(stringifiedNum) // 2
                firstHalf = stringifiedNum[:halfwayPt]
                secondHalf = stringifiedNum[halfwayPt:]

                next_stones[int(firstHalf)] += val
                next_stones[int(secondHalf)] += val

                continue
            
            # 3. Multiply by 2024
            next_stones[int(key * 2024)] += val

        curr_stones = next_stones

    return sum(curr_stones.values())

def part1(initial_stones: List[int]) -> int:
    return blink(initial_stones, 25)

def part2(initial_stones: List[int]) -> int:
    return blink(initial_stones, 75)

def main():
    raw_input: List[str] = read_file(FILEPATH)
    initial_stones: List[int] = [int(s) for s in raw_input[0].split()]

    PART1(part1, initial_stones)
    PART2(part2, initial_stones)

if __name__ == "__main__": main()

