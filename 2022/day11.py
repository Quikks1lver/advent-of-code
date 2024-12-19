from Helpers.FileHelpers import read_file_with_line_breaks
from typing import List, Dict, Callable, Union
import operator
import math
import copy
FILEPATH = "2022/Input/day11.txt"

class Monkey():
    # idea for dict https://stackoverflow.com/questions/5117112/python-convert-a-string-to-an-operator
    operator_dict: Dict[str, Callable] = {
        '+': operator.add,
        '*': operator.mul,
    }

    def __init__(self, s: List[str]) -> None:
        self.id = int(s[0].split()[1][0])
        self.items = [int(x) for x in s[1].strip("Starting items: ").split(',')]
        
        op_info = s[2].strip('Operation: new = old').split()
        second_operand = None if len(op_info) == 1 else int(op_info[1])
        self.op: Callable = lambda old: Monkey.operator_dict[op_info[0]](old, old if second_operand is None else second_operand)

        self.divisor = int(s[3].strip('Test: divisible by'))
        self.test: Callable = lambda x: True if x % self.divisor == 0 else False
        self.true_result: int = int(s[4][-1])
        self.false_result: int = int(s[5][-1])
        self.inspection_count: int = 0

    def add_inspection(self) -> None: self.inspection_count += 1
    def add_item(self, item: int) -> None: self.items.append(item)

    @staticmethod
    def parse_monkeys(filepath: str):
        return [Monkey(line) for line in read_file_with_line_breaks(filepath)]

def play_monkey_in_the_middle(monkees: List[Monkey], num_rounds: int, mod: Union[None, int]) -> List[Monkey]:
    monkeys = [copy.deepcopy(m) for m in monkees]
    for _ in range(num_rounds):
        for m in monkeys:
            while len(m.items) > 0:
                m.add_inspection()
                worry_level = m.items[0]
                worry_level = m.op(worry_level)
                if mod is None: worry_level //= 3
                else: worry_level %= mod

                monkeys[m.true_result if m.test(worry_level) else m.false_result].add_item(worry_level)
                m.items.pop(0)
    return monkeys

def calculate_monkey_business(monkeys: List[Monkey]) -> int:
    inspection_counts = [m.inspection_count for m in monkeys]
    inspection_counts.sort()
    return inspection_counts[-2] * inspection_counts[-1]

def main():
   monkeys = Monkey.parse_monkeys(FILEPATH)
   
   print(f"Part 1 -- {calculate_monkey_business(play_monkey_in_the_middle(monkeys, 20, mod=None))}")

   # I was stuck on how to deal with these big integers, but with the power of ops closed under
   # mod, I was able to solve this. Thanks to link below for the strat.
   # https://aoc.just2good.co.uk/2022/11
   print(f"Part 2 -- {calculate_monkey_business(play_monkey_in_the_middle(monkeys, 10000, mod=math.lcm(*[m.divisor for m in monkeys])))}")

if __name__ == "__main__": main()