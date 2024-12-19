from Helpers.FileHelpers import read_lines
from typing import List
FILEPATH = "2022/Input/day03.txt"

def compute_item_type_value(char: str) -> int:
    total = 0
    total -= (ord('a') if char.islower() else ord('A'))
    total += 26 if char.isupper() else 0
    total += ord(char) + 1
    return total

def sum_shared_priorities(input: List[str]) -> int:
    total = 0
    for s in input:
        total += compute_item_type_value(set(s[:len(s)//2]).intersection(set(s[len(s)//2:])).pop())
    return total

def sum_elf_grouping_priorities(input: List[str]) -> int:
    total = 0
    for i in range(0, len(input), 3):
        total += compute_item_type_value(set(input[i]).intersection(set(input[i+1])).intersection(set(input[i+2])).pop())
    return total

def main():
   input = [line.strip() for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {sum_shared_priorities(input)}")
   print(f"Part 2 -- {sum_elf_grouping_priorities(input)}")

if __name__ == "__main__": main()
# ord() https://www.pythonforbeginners.com/basics/ascii-value-in-python