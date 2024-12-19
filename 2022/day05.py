from Helpers.FileHelpers import read_lines
from typing import List, Tuple
FILEPATH = "2022/Input/day05.txt"

def parse_input(input: List[str]) -> Tuple[List[List[str]], List[Tuple[int, int, int]]]:
    crates = [[] for _ in range(9)]
    directions: List[int, Tuple[int, int]] = list()

    for line in input:
        if line.startswith('['):
            stack_index = 0
            for i in range(len(line)):
                if i % 4 == 0:
                    if line[i] == '[':
                        crates[stack_index].insert(0, line[i+1])
                    stack_index += 1
        elif line.startswith('move'):
            directions.append(tuple([int(ch) for ch in line.split() if ch.isnumeric()]))
    
    return crates, directions

find_tip_of_the_crates = lambda crates: "".join([crate[-1] for crate in crates])

def move_crates_9000(crates: List[List[str]], directions: List[Tuple[int, int, int]]) -> str:
    crates_copy = [_[:] for _ in crates]
    for amount, source, dest in directions:
        for _ in range(amount):
            crates_copy[dest-1].append(crates_copy[source-1].pop())
    return find_tip_of_the_crates(crates_copy)

def move_crates_9001(crates: List[List[str]], directions: List[Tuple[int, int, int]]) -> str:
    crates_copy = [_[:] for _ in crates]
    for amount, source, dest in directions:
        source_crate = crates_copy[source-1]
        for i in range(amount):
            crates_copy[dest-1].append(source_crate[len(source_crate) - amount + i])
        for i in range(amount): source_crate.pop()
    return find_tip_of_the_crates(crates_copy)

def main():
   crates, directions = parse_input([line.strip() for line in read_lines(FILEPATH)])
   print(f"Part 1 -- {move_crates_9000(crates, directions)}")
   print(f"Part 2 -- {move_crates_9001(crates, directions)}")

if __name__ == "__main__": main()