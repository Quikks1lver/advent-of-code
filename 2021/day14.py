from Helpers.FileHelpers import read_lines
from typing import List, Dict
FILEPATH = "2021/Input/day14.txt"

def substitute_polymer_rules(template: str, rules: Dict[str, str], num_steps: int) -> str:
   output_str: str = template
   temp_list: List[str] = [ch for ch in template]
   
   for _ in range(num_steps):
      list_index: int = 0
      
      for str_index in range(len(output_str) - 1):
         substring = output_str[str_index : str_index + 2]
         potential_rule = rules.get(substring, None)
         
         if potential_rule != None:
            temp_list.insert(list_index + 1, potential_rule)
            list_index += 1

         list_index += 1

      output_str = "".join(temp_list)
      print(_)

   return output_str

def calculate_most_minus_least_common_element(s: str) -> int:
   frequencies: Dict[str, int] = dict()

   for ch in s:
      if ch in frequencies.keys():
         frequencies[ch] += 1
      else:
         frequencies[ch] = 1
   
   return max(frequencies.values()) - min(frequencies.values())

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]
   
   polymer_template: str = input_lines[0]
   pair_insertion_rules = [[s for s in line.split(" -> ")] for line in input_lines[2:]]
   pair_insertion_rules: Dict[str, str] = {s[0]: s[1] for s in pair_insertion_rules}

   print(f"Part 1 -- {calculate_most_minus_least_common_element(substitute_polymer_rules(polymer_template, pair_insertion_rules, 10))}")
   # print(f"Part 2 -- {calculate_most_minus_least_common_element(substitute_polymer_rules(polymer_template, pair_insertion_rules, 40))}")

if __name__ == "__main__":
   main()