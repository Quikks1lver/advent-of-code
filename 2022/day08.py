from Helpers.FileHelpers import read_2D_array
from numpy import array
import numpy as np
FILEPATH = "2022/Input/day08.txt"

class TreeHouser():
    def __init__(self, input_file: str) -> None:
        self.trees = array(read_2D_array(input_file, int))
        self.trees_T = self.trees.T    

    def count_visible_trees(self) -> int:
        def is_visible(row: int, col: int) -> int:
            this_tree_height = self.trees[row][col]
            if this_tree_height > max(self.trees_T[col][:row]): # UP
                return True
            if this_tree_height > max(self.trees_T[col][row+1:]): # DOWN
                return True
            if this_tree_height > max(self.trees[row][:col]): # LEFT
                return True
            if this_tree_height > max(self.trees[row][col+1:]): # RIGHT
                return True
            return False
        
        count = 2 * len(self.trees[0]) + 2 * (len(self.trees) - 2)
        for row in range(1, len(self.trees) - 1, 1):
            for col in range(1, len(self.trees[0]) - 1, 1):
                if is_visible(row, col):
                    count += 1
        return count

    def calculate_max_scenic_score(self) -> int:
        def calculate_scenic_score(row: int, col: int):
            up = np.flip(self.trees_T[col][:row])
            down = self.trees_T[col][row+1:]
            left = np.flip(self.trees[row][:col])
            right = self.trees[row][col+1:]

            this_tree_height = self.trees[row][col]
            score = 1

            for direction in (up, down, left, right):
                count = 0
                for other_height in direction:
                    count += 1
                    if other_height >= this_tree_height:
                        break
                score *= count

            return score
        
        max_scenic_score = 0
        for row in range(1, len(self.trees) - 1, 1):
            for col in range(1, len(self.trees[0]) - 1, 1):
                max_scenic_score = max(max_scenic_score, calculate_scenic_score(row, col))

        return max_scenic_score
        
def main():
    houser = TreeHouser(FILEPATH)
    print(f"Part 1 -- {houser.count_visible_trees()}")
    print(f"Part 2 -- {houser.calculate_max_scenic_score()}")

if __name__ == "__main__": main()