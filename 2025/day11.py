from frozendict import frozendict
from functools import lru_cache
from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import Dict, Tuple
FILEPATH = "2025/Input/day11.txt"

# Note: will need to install frozendict for this problem.

START = 'you'
END = 'out'
SVR = 'svr'
DAC = 'dac'
FFT = 'fft'

@lru_cache
def count_paths(curr: str, mapping: frozendict) -> int: # type: ignore
    return 1 if curr == END else sum([count_paths(v, mapping) for v in mapping[curr]])

@lru_cache
def count_paths_with_constraints(curr: str, mapping: frozendict, visited_dac: bool, visited_fft: bool) -> int: # type: ignore
    if curr == END: return 1 if visited_dac and visited_fft else 0
    if curr == DAC: visited_dac = True
    if curr == FFT: visited_fft = True
    return sum([count_paths_with_constraints(v, mapping, visited_dac, visited_fft) for v in mapping[curr]])

def part1(mapping: Dict[str, Tuple[str, ...]]) -> int:
    return count_paths(START, frozendict(mapping))

def part2(mapping: Dict[str, Tuple[str, ...]]) -> int:
    return count_paths_with_constraints(SVR, frozendict(mapping), False, False)

def main() -> None:
    mapping: Dict[str, Tuple[str, ...]] = dict()

    for line in read_lines(FILEPATH):
        split_line = line.split(':')
        mapping[split_line[0].strip()] = tuple([v for v in split_line[1].strip().split() if not v.isspace()])

    PART1(part1, mapping) # 0.25 ms
    PART2(part2, mapping) # 15 s

if __name__ == "__main__": main()
