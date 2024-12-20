# Apparently, problem says we need BIG numbers here, so using Python for ease-of-use.
# After finishing Part 1, I probably could've used C++ anyway ... :D

from PythonHelpers.FileHelpers import read_file
from PythonHelpers.PrintSolution import PART1, PART2
from typing import List
FILEPATH = "2024/Input/day09.txt"

FREE_SPACE: int = -1

def compute_checksum(file_str: List[int]) -> int:
    checksum = 0
    for i, val in enumerate(file_str):
        checksum += (0 if val == FREE_SPACE else i * val)
    return checksum

def construct_file_system(input_str: str) -> List[int]:
    file_system: List[int] = []
    counter = 0

    for i, val in enumerate(input_str):        
        file_system.extend([counter if i % 2 == 0 else FREE_SPACE] * int(val))
        if i % 2 == 0:
            counter += 1
    
    return file_system

def part1(input_str: str) -> int:
    file_system: List[int] = construct_file_system(input_str)
    
    left_ptr = 0
    right_ptr = len(file_system) - 1

    while True:
        # Grab a free space.
        while left_ptr < len(file_system) and file_system[left_ptr] != FREE_SPACE:
            left_ptr += 1
        if left_ptr >= len(file_system):
            break

        # Grab a value that can be shifted to a free space.
        while right_ptr >= 0 and file_system[right_ptr] == FREE_SPACE:
            right_ptr -= 1
        if right_ptr < 0:
            break

        if left_ptr > right_ptr:
            break

        file_system[left_ptr] = file_system[right_ptr]
        file_system[right_ptr] = FREE_SPACE
        left_ptr += 1
        right_ptr -= 1

    return compute_checksum(file_system)

def part2(input_str: str) -> int:
    file_system: List[int] = construct_file_system(input_str)

    file_end_ptr = len(file_system) - 1
    file_size = 0
    processed_files = set()

    while file_end_ptr >= 0:        
        # Grab latest block that can be shifted to a free space.
        while file_end_ptr >= 0 and file_system[file_end_ptr] == FREE_SPACE:
            file_end_ptr -= 1
        if file_end_ptr < 0:
            break

        # Calculate the file size of that block.
        file_size = 0
        file_val = file_system[file_end_ptr]
        while file_end_ptr - file_size >= 0 and file_system[file_end_ptr - file_size] == file_val:
            file_size += 1
        
        # Don't move processed files again.
        if file_val in processed_files:
            file_end_ptr -= file_size
            continue
        
        # Find a free space, then calculate how many are in the chunk.
        free_block_size = 0
        free_block_start_ptr = 0 # Could optimize this, but will suffice to start from LHS for now.
        
        while free_block_size < file_size:
            free_block_start_ptr += free_block_size
            free_block_size = 0

            while free_block_start_ptr < len(file_system) \
                and file_system[free_block_start_ptr] != FREE_SPACE:
                free_block_start_ptr += 1
            if free_block_start_ptr >= len(file_system):
                break
            
            while free_block_start_ptr + free_block_size < len(file_system) \
                and file_system[free_block_start_ptr + free_block_size] == FREE_SPACE:
                free_block_size += 1

            # Ensure free space is large enough and to left of file.
            # I had a nasty bug here ...
            # My original left/right check was this: free_block_start_ptr + free_block_size < file_end_ptr - file_size:
            # I only need to look at left-most AKA start pointers for each chunk.
            if free_block_size >= file_size \
                and free_block_start_ptr < file_end_ptr - file_size:

                for i in range(file_size):
                    file_system[free_block_start_ptr + i] = file_val
                    file_system[file_end_ptr - i] = FREE_SPACE
                break
        
        # Move to next file, R -> L
        processed_files.add(file_val)
        file_end_ptr -= file_size

    return compute_checksum(file_system)

def main():   
    input_str: str = read_file(FILEPATH)[0]

    PART1(part1, input_str)

    print("Part 2 takes ~14s on my M1 machine.")
    PART2(part2, input_str)

if __name__ == "__main__": main()