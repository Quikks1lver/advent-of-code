from Helpers.FileHelpers import read_lines
from typing import List, Dict, NewType
FILEPATH = "2021/Input/day14.txt"

def substitute_polymer_rules(template: str, rules: Dict[str, str], num_steps: int) -> List[str]:
   ch_list: List[str] = [ch for ch in template]
   
   for _ in range(num_steps):
      index = 0
      
      while index < len(ch_list) - 1:
         substring = ch_list[index] + ch_list[index + 1]
         potential_rule = rules.get(substring, None)
         
         if potential_rule != None:
            ch_list.insert(index + 1, potential_rule)
            index += 1

         index += 1

   return ch_list

def calculate_most_minus_least_common_element(s: List[str]) -> int:
   frequencies: Dict[str, int] = dict()

   for ch in s:
      if ch in frequencies.keys():
         frequencies[ch] += 1
      else:
         frequencies[ch] = 1
   
   return max(frequencies.values()) - min(frequencies.values())

def update_dict_with_value(d: Dict[str, int], key: str, val: int) -> None:
   """
   Updates a dictionary with the given integer value (adding to current val),
   or initializing the key to the given value
   """   
   if key not in d.keys():
      d[key] = val
   else:
      d[key] += val

def substitute_polymer_rules_optimized(template: str, rules: Dict[str, str], num_steps: int) -> Dict[str, int]:
   old_map: Dict[str, int] = dict()
   letter_map: Dict[str, int] = dict()

   for index in range(len(template) - 1):
      substring = template[index : index + 2]
      update_dict_with_value(old_map, substring, 1)

   for ch in template:
      update_dict_with_value(letter_map, ch, 1)
   
   for _ in range(num_steps):
      new_map = old_map.copy()

      for substring, num_occurrences in old_map.items():
         potential_rule = rules.get(substring, None)
         num_occurrences = old_map[substring]

         if num_occurrences != 0 and potential_rule != None:            
            new_map[substring] -= num_occurrences
            update_dict_with_value(letter_map, potential_rule, num_occurrences)
            update_dict_with_value(new_map, substring[0] + potential_rule, num_occurrences)
            update_dict_with_value(new_map, potential_rule + substring[1], num_occurrences)

      old_map = new_map
   
   return letter_map

def calculate_most_minus_least_common_element_dict_version(letter_map: Dict[str, int]) -> int:
   return max(letter_map.values()) - min(letter_map.values())

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]
   
   polymer_template: str = input_lines[0]
   pair_insertion_rules = [[s for s in line.split(" -> ")] for line in input_lines[2:]]
   pair_insertion_rules: Dict[str, str] = {s[0]: s[1] for s in pair_insertion_rules}

   print(f"Part 1 -- {calculate_most_minus_least_common_element(substitute_polymer_rules(polymer_template, pair_insertion_rules, 10))}")
   print(f"Part 2 -- {calculate_most_minus_least_common_element_dict_version(substitute_polymer_rules_optimized(polymer_template, pair_insertion_rules, 40))}")

if __name__ == "__main__":
   main()