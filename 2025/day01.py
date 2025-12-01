from PythonHelpers.FileHelpers import read_lines
from PythonHelpers.PrintSolution import *
from typing import List, Tuple
FILEPATH = "2025/Input/day01.txt"

def main():
   input: List[str] = [(line[:1], int(line[1:].strip())) for line in read_lines(FILEPATH)]

if __name__ == "__main__": main()