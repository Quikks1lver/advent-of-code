from Helpers.FileHelpers import read_lines
from typing import List, Union
FILEPATH = "2022/Input/day10.txt"

def its_cathode_ray_time(input: List[List[str]], part1: bool) -> Union[int, None]:
    def add_signal_strength(signal_strength: int, x: int, clock_cycle: int) -> int:
        if clock_cycle == 20 or (clock_cycle + 20) % 40 == 0:
            return signal_strength + x * clock_cycle
        return signal_strength

    def print_sprite(x: int, clock_cycle: int) -> None:
        if (clock_cycle-1) % 40 in [x, x-1, x+1]: print('#', end='')
        else: print(' ', end='')
        if clock_cycle % 40 == 0: print()
    
    clock_cycle = 0
    input_i = 0
    x = 1
    signal_strength = 0
    wait = True

    while input_i < len(input):
        clock_cycle += 1

        if part1:
            signal_strength = add_signal_strength(signal_strength, x, clock_cycle)
        else:
            print_sprite(x, clock_cycle)

        instruction = input[input_i]

        if instruction[0] == 'noop':
            input_i += 1
        else:
            if wait:
                wait = False
            else:
                input_i += 1
                wait = True
                x += int(instruction[1])
        
    return signal_strength if part1 else None

def main():
   input: List[List[str]] = [line.strip().split() for line in read_lines(FILEPATH)]
   
   # I was approaching this problem wrong, so thanks to Jonathan Paulson on YouTube for the strats!
   print(f"Part 1 -- {its_cathode_ray_time(input, True)}")
   print(f"Part 2 -- RLEZFLGE {its_cathode_ray_time(input, False)}")
   

if __name__ == "__main__": main()