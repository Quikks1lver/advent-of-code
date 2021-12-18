from Helpers.FileHelpers import read_lines
from typing import Dict, List, Set, Tuple
FILEPATH = "2021/Input/day12.txt"

PRINT_PATHS = False  # toggle to see all paths!
START_CAVE = "start"
END_CAVE = "end"

def is_small_cave(cave: str) -> bool:
   if cave == START_CAVE or cave == END_CAVE:
      return False
   return cave.islower()

def find_number_of_cave_traversals(cave_map: Dict[str, List[str]]) -> int:
   return find_number_of_cave_traversals_recursive_dfs_helper(cave_map, set(), set(), START_CAVE, None, [START_CAVE])

def find_number_of_cave_traversals_recursive_dfs_helper(cave_map: Dict[str, List[str]], visited_small_caves: Set[str], visited_moves: Set[Tuple[str, str]], cur_cave: str, have_visited_a_small_cave_twice: str, path_traversal: List[str]) -> int:
   if cur_cave == END_CAVE:
      if PRINT_PATHS:
         print(path_traversal)
      return 1

   num_traversals = 0

   for next_cave in cave_map[cur_cave]:
      if next_cave not in visited_small_caves:
         if next_cave == START_CAVE:
            continue
         
         move = (cur_cave, next_cave)
         # if move in visited_moves:
         #    continue
         
         new_visited_small_caves = visited_small_caves.copy()
         if is_small_cave(next_cave):
            new_visited_small_caves.add(next_cave)
         new_visited_moves = visited_moves.copy()
         new_visited_moves.add(move)
         new_path_traversal = path_traversal.copy()
         new_path_traversal.append(next_cave)
         
         # call recursive function again
         num_traversals += find_number_of_cave_traversals_recursive_dfs_helper(cave_map, new_visited_small_caves, new_visited_moves, next_cave, have_visited_a_small_cave_twice, new_path_traversal)
      
      elif have_visited_a_small_cave_twice == None:
         move = (cur_cave, next_cave)
         # if move in visited_moves:
         #    continue
         
         new_visited_small_caves = visited_small_caves.copy()
         if is_small_cave(next_cave):
            new_visited_small_caves.add(next_cave)
         new_visited_moves = visited_moves.copy()
         new_visited_moves.add(move)
         new_path_traversal = path_traversal.copy()
         new_path_traversal.append(next_cave)
         
         # call recursive function again
         num_traversals += find_number_of_cave_traversals_recursive_dfs_helper(cave_map, new_visited_small_caves, new_visited_moves, next_cave, next_cave, new_path_traversal)

   return num_traversals

def create_cave_map(cave_connections_raw: List[Tuple[str]]) -> Dict[str, List[str]]:
   cave_map: Dict[str, List[str]] = dict()

   # create a two way mapping between caves
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

   print(f"Part 1 -- {find_number_of_cave_traversals(cave_map)}")
   # find_number_of_cave_traversals(cave_map)
   # print(f"Part 2 -- {}")

if __name__ == "__main__":
   main()