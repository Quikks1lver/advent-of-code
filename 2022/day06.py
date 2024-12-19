from Helpers.FileHelpers import read_lines
FILEPATH = "2022/Input/day06.txt"

def start_marker(input: str, num_diffs: int) -> int:
    for index in range(len(input) - num_diffs + 1):
        if len(set(input[index : index + num_diffs])) == num_diffs:
            return index + num_diffs

def main():
   input: str = [line.strip() for line in read_lines(FILEPATH)][0]
   print(f"Part 1 -- {start_marker(input, 4)}")
   print(f"Part 2 -- {start_marker(input, 14)}")

if __name__ == "__main__": main()