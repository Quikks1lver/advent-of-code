from heapq import heappop, heappush
from Helpers.FileHelpers import read_lines
from typing import List, Tuple
FILEPATH = "2022/Input/day12.txt"

def convert_map_into_ints(input: List[str]) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    parse_char = lambda c: ord(c) - ord('a') if c.islower() else c
    map: List[List[int]] = [[parse_char(col) for col in row.strip()] for row in input]
    
    for i, r in enumerate(map):
        for j, c in enumerate(r):
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                end = (i, j)
    
    return (map, start, end)

def dijkstras(graph: List[List[int]], start: Tuple[int, int]) -> List[List[int]]:
    oo = 1e8 # infinity

    distances: List[List[int]] = [[oo for c in r] for r in graph]
    visited: List[List[bool]] = [[False for c in r] for r in graph]
    
    # https://docs.python.org/3/library/heapq.html
    # (key, value) = (distance, (x, y)) pairs
    minheap: List[Tuple[int, Tuple[int, int]]] = []
    distances[start[0]][start[1]] = 0
    heappush(minheap, (0, start))

    is_inbounds = lambda x, y: True if x >= 0 and x < len(graph) and y >= 0 and y < len(graph[0]) else False
    is_reachable = lambda start_x, start_y, end_x, end_y: True if graph[end_x][end_y] <= graph[start_x][start_y] or graph[end_x][end_y] == graph[start_x][start_y] + 1 else False

    while len(minheap) > 0:
        pullout_dist, (pullout_row, pullout_col) = heappop(minheap)
        
        if visited[pullout_row][pullout_col]:
            continue
        
        visited[pullout_row][pullout_col] = True

        # down, up, left, right
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_point = (pullout_row + d_row, pullout_col + d_col)
            if is_inbounds(new_point[0], new_point[1]) and is_reachable(pullout_row, pullout_col, new_point[0], new_point[1]):
                new_dist = pullout_dist + 1
                if new_dist < distances[new_point[0]][new_point[1]]:
                    distances[new_point[0]][new_point[1]] = new_dist
                    heappush(minheap, (new_dist, new_point))

    return distances

def find_best_start(graph: List[List[int]], end: Tuple[int, int]) -> int:    
    minheap = []
    for i, r in enumerate(graph):
        for j, c in enumerate(r):
            if c == 0:
                distances = dijkstras(graph, (i, j))
                heappush(minheap, distances[end[0]][end[1]])
    return heappop(minheap)

def main():
   map, start, end = convert_map_into_ints(read_lines(FILEPATH))
   map[start[0]][start[1]] = 0
   map[end[0]][end[1]] = ord('z') - ord('a')

   print(f"Part 1 -- {dijkstras(map, start)[end[0]][end[1]]}")
   print(f"Part 2 -- {find_best_start(map, end)}")

if __name__ == "__main__": main()