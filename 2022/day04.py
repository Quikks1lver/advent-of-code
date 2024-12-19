from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2022/Input/day04.txt"

def contains_range_count(input: List[List[int]]) -> int:
    count = 0
    for (a, b), (c, d) in input:
        if a <= c and b >= d or c <= a and d >= b:
            count += 1
    return count

def overlaps_count(input: List[List[int]]) -> int:
    count = 0
    for (a, b), (c, d) in input:
        set1 = {_ for _ in range(a, b + 1, 1)}
        set2 = {_ for _ in range(c, d + 1, 1)}
        count += 1 if len(set1.intersection(set2)) > 0 else 0
    return count

def main():
   input: List[List[int]] = [[[int(x) for x in _.split(sep='-')] for _ in line.strip().split(sep=',')] for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {contains_range_count(input)}")
   print(f"Part 2 -- {overlaps_count(input)}")

if __name__ == "__main__": main()