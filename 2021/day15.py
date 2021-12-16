from heapq import heappop, heappush
from Helpers.ArrayHelpers import is_inbounds
from Helpers.FileHelpers import read_2D_array
from sys import maxsize
from typing import Dict, List, Tuple
FILEPATH = "2021/Input/day15.txt"

MOVES: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class NodeVal():
   def __init__(self, cost: int, adj_nodes: List[Tuple[int, int]]):
      self.cost = cost
      self.adj_nodes = adj_nodes

def create_node_map(risk_matrix: List[List[int]]) -> Dict[Tuple[int, int], NodeVal]:
   node_map: Dict[Tuple[int, int], NodeVal] = dict()
   
   for x in range(len(risk_matrix)):
      for y in range(len(risk_matrix[0])):
         adj_list = []

         for (dx, dy) in MOVES:
            new_x, new_y = x + dx, y + dy
            if is_inbounds(risk_matrix, new_x, new_y):
               adj_list.append((new_x, new_y))
         
         node_map[(x, y)] = NodeVal(risk_matrix[x][y], adj_list)
   
   return node_map

def dijkstras_algorithm(node_map: Dict[Tuple[int, int], NodeVal], source: Tuple[int, int]) -> List[List[int]]:
   dist: Dict[Tuple[int, int], int] = {key : maxsize for key in node_map.keys()}
   visited = set()
   
   dist[source] = 0
   visited_node_count = 0

   # https://docs.python.org/3/library/heapq.html
   # you can use tuples in minheaps; "key" is dist, and "val" is actual node tuple
   minheap: List[Tuple[int, Tuple[int, int]]] = []
   heappush(minheap, (dist[source], source))

   while len(minheap) > 0 and visited_node_count < len(node_map.keys()):
      pullout_node = heappop(minheap)[1]
      if pullout_node in visited:
         continue

      visited.add(pullout_node)
      visited_node_count += 1

      pullout_node_val = node_map[pullout_node]

      for key in pullout_node_val.adj_nodes:
         new_dist = dist[pullout_node] + node_map[key].cost

         if new_dist < dist[key]:
            dist[key] = new_dist
            heappush(minheap, (dist[key], key))

   return dist

def get_new_risk(risk_matrix: List[List[int]], row: int, col: int, x_block: int, y_block: int) -> int:
   curr_risk_level = risk_matrix[row][col]
   val = curr_risk_level + x_block + y_block
   if val > 10:
      val += 1
   val %= 10
   return val if val != 0 else 1

def expand_risk_matrix(risk_matrix: List[List[int]]) -> List[List[int]]:
   new_matrix = [[c for c in r] for r in risk_matrix]
   
   for _ in range(len(risk_matrix) * 4):
      new_matrix.append(list())
   
   for x_block in range(5):
      for y_block in range(5):
         if not (x_block == 0 and y_block == 0):
            for row in range(len(risk_matrix)):
               for col in range(len(risk_matrix[0])):
                  new_matrix[(x_block * len(risk_matrix)) + row].append(get_new_risk(risk_matrix, row, col, x_block, y_block))

   return new_matrix

def main():
   # after working in vain on this problem, I checked the subreddit, which recommended Dijkstra's!

   risk_matrix: List[List[int]] = read_2D_array(FILEPATH, int)
   node_map: Dict[Tuple[int, int], NodeVal] = create_node_map(risk_matrix)
   print(f"Part 1 -- {dijkstras_algorithm(node_map, (0, 0))[len(risk_matrix) - 1, len(risk_matrix[0]) - 1]}")
   
   new_matrix = expand_risk_matrix(risk_matrix)
   node_map = create_node_map(new_matrix)
   print(f"Part 2 -- {dijkstras_algorithm(node_map, (0, 0))[len(new_matrix) - 1, len(new_matrix[0]) - 1]}")

if __name__ == "__main__":
   main()