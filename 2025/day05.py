from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import List, Set, Tuple
FILEPATH = "2025/Input/day05.txt"

def part1(ranges: List[Tuple[int, int]], ingredients: List[int]) -> int:
    ingredients_set: Set[int] = set(ingredients)
    starting_len = len(ingredients_set)

    for start, end in ranges:
        fresh_ingredients: Set[int] = set()
        
        for ingredient in ingredients_set:
            if start <= ingredient <= end:
                fresh_ingredients.add(ingredient)

        ingredients_set.difference_update(fresh_ingredients)

    return starting_len - len(ingredients_set)

def generate_range_set(ranges: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    new_ranges: Set[Tuple[int, int]] = set()
    new_ranges.add(ranges[0])
    
    for i in range(1, len(ranges)):
        start, end = ranges[i]
        removed_ranges: Set[Tuple[int, int]] = set()
        
        for new_range_start, new_range_end in new_ranges:
            if (new_range_start <= start <= new_range_end) or (new_range_start <= end <= new_range_end):
                start = min(start, new_range_start)
                end = max(end, new_range_end)
                removed_ranges.add((new_range_start, new_range_end))

        new_ranges.difference_update(removed_ranges)
        new_ranges.add((start, end))

    return new_ranges

def part2(ranges: List[Tuple[int, int]]) -> int:
    new_ranges_initial = generate_range_set(ranges)
    new_ranges_after_initial_pass_to_dedupe = generate_range_set(list(new_ranges_initial))
    return sum((end-start+1) for start, end in new_ranges_after_initial_pass_to_dedupe)

def main() -> None:
    ranges: List[Tuple[int, int]] = []
    ingredients: List[int] = []
    first_half = True

    for line in read_lines(FILEPATH):
        if len(line) == 0:
            first_half = False
            continue
        if first_half:
            end_pts = line.split('-')
            ranges.append((int(end_pts[0]), int(end_pts[1])))
        else:
            ingredients.append(int(line))
    
    PART1(part1, ranges, ingredients)
    PART2(part2, ranges)

if __name__ == "__main__": main()
