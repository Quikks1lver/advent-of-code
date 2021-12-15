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

def substitute_polymer_rules_optimized(template: str, rules: Dict[str, str], num_steps: int):
   old_map: Dict[str, int] = dict()
   letter_map: Dict[str, int] = dict()
   
   # letter and old map
   for index in range(len(template) - 1):
      letter = template[index]
      if letter not in letter_map.keys():
         letter_map[letter] = 1
      else:
         letter_map[letter] += 1
      
      substring = template[index : index + 2]
      if substring not in old_map.keys():
         old_map[substring] = 1
      else:
         old_map[substring] += 1
   
   letter = template[-1]
   if letter not in letter_map.keys():
      letter_map[letter] = 1
   else:
      letter_map[letter] += 1
   # ======================

   for _ in range(num_steps):
      new_map = old_map.copy()

      for key in old_map.keys():
         potential_rule = rules.get(key, None)
         num_occurrences = old_map[key]

         if num_occurrences == 0:
            continue

         if potential_rule != None:
            old_substring = key
            new_substring_1 = old_substring[0] + potential_rule
            new_substring_2 = potential_rule + old_substring[1]

            # print(f"{key} => {new_substring_1} {new_substring_2}")
            
            letter = potential_rule
            if letter not in letter_map.keys():
               letter_map[letter] = num_occurrences
            else:
               letter_map[letter] += num_occurrences

            new_map[key] -= num_occurrences
            if new_substring_1 not in new_map.keys():
               new_map[new_substring_1] = num_occurrences
            else:
               new_map[new_substring_1] += num_occurrences
            
            if new_substring_2 not in new_map.keys():
               new_map[new_substring_2] = num_occurrences
            else:
               new_map[new_substring_2] += num_occurrences

      old_map = new_map
      # print(old_map)
      # print(letter_map)
      # print("-------------------------")
   
   return letter_map

def main():
   input_lines = [line.strip() for line in read_lines(FILEPATH)]
   
   polymer_template: str = input_lines[0]
   pair_insertion_rules = [[s for s in line.split(" -> ")] for line in input_lines[2:]]
   pair_insertion_rules: Dict[str, str] = {s[0]: s[1] for s in pair_insertion_rules}

   # print(f"Part 1 -- {calculate_most_minus_least_common_element(substitute_polymer_rules(polymer_template, pair_insertion_rules, 10))}")
   # print(f"Part 2 -- {calculate_most_minus_least_common_element(substitute_polymer_rules(polymer_template, pair_insertion_rules, 40))}")

   h = substitute_polymer_rules_optimized(polymer_template, pair_insertion_rules, 40)
   print(h)
   print(max(h.values()) - min(h.values()))

if __name__ == "__main__":
   main()