from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2025/Input/day09.txt"
DIMENSION = -1

Point = Tuple[int, int]

def calculate_area(p1: Point, p2: Point) -> int:
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def part1(input: List[Point]) -> int:
    maximum_area = -1

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            area = calculate_area(input[i], input[j])
            if area > maximum_area:
                maximum_area = area
    
    return maximum_area

def main() -> None:
    input: List[Point] = [tuple([int(ch) for ch in line.split(',')]) for line in read_lines(FILEPATH)] # type: ignore

    PART1(part1, input)
    # Spent a lot of time on part 2. Going to commit part 1 for now.

if __name__ == "__main__": main()
