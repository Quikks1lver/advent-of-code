from Helpers.FileHelpers import read_lines
from typing import Dict, List, Set, Tuple
FILEPATH = "2021/Input/day12.txt"

START_CAVE = "start"
END_CAVE = "end"

def is_small_cave(cave: str) -> bool:
   if cave == START_CAVE or cave == END_CAVE:
      return False
   return cave.islower()

def is_big_cave(cave: str) -> bool:
   return not is_small_cave(cave)

def find_number_of_cave_traversals(cave_map: Dict[str, List[str]], visited_small_caves: Set[str], visited_moves: Set[Tuple[str, str]], cur_cave: str, here: List[str]) -> int:
   if cur_cave == END_CAVE:
      print("======")
      print(here)
      print("======")
      return 1

   num_traversals = 0

   for next_cave in cave_map[cur_cave]:
      if is_small_cave(next_cave) and next_cave in visited_small_caves:
         continue

      if next_cave == START_CAVE:
         continue

      move = (cur_cave, next_cave)
      if move in visited_moves:
         continue

      new_visited = visited_small_caves.copy()
      if is_small_cave(next_cave):
         new_visited.add(next_cave)

      visited_moves2 = visited_moves.copy()
      visited_moves2.add(move)
      here2 = here.copy()
      here2.append(next_cave)
      num_traversals += find_number_of_cave_traversals(cave_map, new_visited, visited_moves2, next_cave, here2)

   return num_traversals

def create_cave_map(cave_connections_raw: List[Tuple[str]]) -> Dict[str, List[str]]:
   cave_map: Dict[str, List[str]] = dict()

   for (start_cave, end_cave) in cave_connections_raw:
      if start_cave in cave_map.keys():
         cave_map[start_cave].append(end_cave)
      else:
         cave_map[start_cave] = [end_cave]

      if end_cave in cave_map.keys():
         cave_map[end_cave].append(start_cave)
      else:
         cave_map[end_cave] = [start_cave]
   
   return cave_map

def main():
   cave_connections_raw: List[Tuple[str, str]] = [tuple(line.strip().split("-")) for line in read_lines(FILEPATH)]
   cave_map: Dict[str, List[str]] = create_cave_map(cave_connections_raw)
   val = find_number_of_cave_traversals(cave_map, set(), set(), START_CAVE, ["start"])
   print(val)

   # print(f"Part 1 -- {}")
   # print(f"Part 2 -- {}")

if __name__ == "__main__":
   main()