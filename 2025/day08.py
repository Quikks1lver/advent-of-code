import heapq
import math
from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import FrozenSet, List, Set, Tuple
FILEPATH = "2025/Input/day08.txt"

# Good learning from today: Python does not allow sets of sets because you need to be
# able to hash sets correctly and sets are mutable. Frozen sets are immutable and hence
# you can have a set of *frozen sets*.

# Type aliases
Point = Tuple[int, int, int]
Minheap = List[Tuple[float, Tuple[Point, Point]]]

DEFAULT_POINT = (-1, -1, -1)

def calculate_euclidean_distance(p1: Point, p2: Point) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 + 
        (p2[1] - p1[1]) ** 2 + 
        (p2[2] - p1[2]) ** 2
    )

# Minheap of distances, and each element is [distance, [Point1, Point2]]
def create_distances_minheap(input: List[Point]) -> Minheap:
    distances_minheap: Minheap = []

    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if i >= len(input) or j >= len(input):
                continue
            
            p1, p2 = input[i], input[j]
            euclidean_distance = calculate_euclidean_distance(p1, p2)

            heapq.heappush(distances_minheap, (euclidean_distance, (p1, p2)))
    
    return distances_minheap

def part1(input: List[Point], num_iters: int) -> int:
    distances_minheap = create_distances_minheap(input)
    circuits: Set[FrozenSet[Point]] = set()

    for _ in range(num_iters):
        popped_val: Tuple[float, Tuple[Point, Point]] = heapq.heappop(distances_minheap)
        p1, p2 = popped_val[1]
        set_to_add: Set[Point] = {p1, p2}
        sets_to_remove: Set[FrozenSet[Point]] = set()

        for circuit in circuits:
            if p1 in circuit or p2 in circuit:
                sets_to_remove.add(frozenset(circuit.copy()))
                
                for item in circuit:
                    set_to_add.add(item)
        
        circuits.difference_update(sets_to_remove)
        circuits.add(frozenset(set_to_add))

    sorted_circuit_sizes = [len(set_within) for set_within in circuits]
    sorted_circuit_sizes.sort()
    return math.prod(sorted_circuit_sizes[-3:])

def part2(input: List[Point]) -> int:
    input_set: Set[Point] = set(input)
    mega_circuit: Set[Point] = set()

    minheap = create_distances_minheap(input)

    while len(mega_circuit) != len(input):
        while True:
            popped_val = heapq.heappop(minheap)
            p1, p2 = popped_val[1]

            if p1 not in mega_circuit or p2 not in mega_circuit:
                break

        # Using discard() instead of remove() to avoid key not found exception.
        mega_circuit.add(p1)
        mega_circuit.add(p2)
        input_set.discard(p1)
        input_set.discard(p2)

    return p1[0] * p2[0]

def main() -> None:
    input: List[Point] = []
    for line in read_lines(FILEPATH):
        single_line: List[int] = []
        for v in line.split(','):
            single_line.append(int(v))
        input.append(tuple(single_line)) # type: ignore

    PART1(part1, input, 1000)

    # Initial part 2 solution I recalculated distances every time, and took 190s, but got right
    # answer. Then I realized ... wait we can still use minheap. New solution takes <1s.
    PART2(part2, input)

if __name__ == "__main__": main()
