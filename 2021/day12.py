from collections import defaultdict
from Helpers.FileHelpers import read_lines
from typing import Dict, List, Set, Tuple, Union
FILEPATH = "2021/Input/day12.txt"

PRINT_PATHS = False  # toggle to see all paths!
START_CAVE = "start"
END_CAVE = "end"

def is_small_cave(cave: str) -> bool:
   if cave == START_CAVE or cave == END_CAVE:
      return False
   return cave.islower()

def create_visited_cave_and_path_traversal_copies(visited_small_caves: Set[str], path_traversal: List[str], next_cave: str) -> Tuple[Set[str], List[str]]:
   new_visited_small_caves = visited_small_caves.copy()
   if is_small_cave(next_cave):
      new_visited_small_caves.add(next_cave)
   new_path_traversal = path_traversal.copy()
   new_path_traversal.append(next_cave)
   return (new_visited_small_caves, new_path_traversal)

def find_number_of_cave_traversals(cave_map: Dict[str, List[str]], is_part_one: bool) -> int:
   return find_number_of_cave_traversals_recursive_dfs_helper(cave_map, set(), START_CAVE, is_part_one if is_part_one else None, [START_CAVE])

def find_number_of_cave_traversals_recursive_dfs_helper(cave_map: Dict[str, List[str]], visited_small_caves: Set[str], cur_cave: str, have_visited_cave_twice: Union[bool, str], path_traversal: List[str]) -> int:
   if cur_cave == END_CAVE:
      if PRINT_PATHS:
         print(path_traversal)
      return 1

   num_traversals = 0

   for next_cave in cave_map[cur_cave]:
      if next_cave == START_CAVE:
            continue
      
      elif next_cave not in visited_small_caves:
         new_visited_small_caves, new_path_traversal = create_visited_cave_and_path_traversal_copies(visited_small_caves, path_traversal, next_cave)
         num_traversals += find_number_of_cave_traversals_recursive_dfs_helper(cave_map, new_visited_small_caves, next_cave, have_visited_cave_twice, new_path_traversal)
      
      elif have_visited_cave_twice == None:         
         new_visited_small_caves, new_path_traversal = create_visited_cave_and_path_traversal_copies(visited_small_caves, path_traversal, next_cave)
         num_traversals += find_number_of_cave_traversals_recursive_dfs_helper(cave_map, new_visited_small_caves, next_cave, next_cave, new_path_traversal)

   return num_traversals

def create_cave_map(cave_connections_raw: List[Tuple[str]]) -> Dict[str, List[str]]:
   cave_map: Dict[str, List[str]] = defaultdict(list)

   # create a two way mapping between caves
   for (start_cave, end_cave) in cave_connections_raw:
         cave_map[start_cave].append(end_cave)
         cave_map[end_cave].append(start_cave)
   
   return cave_map

def main():
   cave_connections_raw: List[Tuple[str, str]] = [tuple(line.strip().split("-")) for line in read_lines(FILEPATH)]
   cave_map: Dict[str, List[str]] = create_cave_map(cave_connections_raw)

   print(f"Part 1 -- {find_number_of_cave_traversals(cave_map, True)}")
   
   # I was struggling on part 2 since my if-checks were out of order; thanks to Jonathan Paulson for the help on YouTube!
   print(f"Part 2 -- {find_number_of_cave_traversals(cave_map, False)}")

if __name__ == "__main__":
   main()