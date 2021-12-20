from collections import defaultdict
from Helpers.FileHelpers import read_lines
from typing import DefaultDict, List, Set, Tuple
FILEPATH = "2021/Input/day08.txt"

SEV_SEG_EZ_NUM_LENGTHS = {2, 3, 4, 7}

def parse_input(input_lines: List[str]) -> Tuple[List[List[Set[str]]], List[List[str]]]:
   signal_patterns: List[List[Set[str]]] = []
   output_values: List[List[str]] = []

   for _ in input_lines:
      s = _.split("|")
      
      new_list: List[Set[str]] = []
      for string in s[0].split():
         new_set: Set[str] = set()
         for ch in string:
            new_set.add(ch)
         new_list.append(new_set)
      
      signal_patterns.append(new_list)
      output_values.append(s[1].split())

   return signal_patterns, output_values

def count_easy_digits(output_values: List[List[str]]) -> int:
   count = 0
   
   for row in output_values:
       for string in row:
          if len(string) in SEV_SEG_EZ_NUM_LENGTHS:
             count += 1
   
   return count

def create_seven_segment_num_map(signal_patterns: List[Set[str]]) -> DefaultDict[int, Set[str]]:
   # a whole lot of set properties!

   num_dict: DefaultDict[int, Set[str]] = defaultdict(set)
   letter_mapping: DefaultDict[str, str] = defaultdict(str)
   
   # obtaining 1, 4, 7, and 8
   for signal_set in signal_patterns:
      if len(signal_set) == 2:
         num_dict[1] = signal_set
      elif len(signal_set) == 3:
         num_dict[7] = signal_set
      elif len(signal_set) == 4:
         num_dict[4] = signal_set
      elif len(signal_set) == 7:
         num_dict[8] = signal_set
   
   six_symbols: List[Set[str]] = [s for s in signal_patterns if len(s) == 6]

   # obtaining "a"
   letter_mapping["a"] = num_dict[7].difference(num_dict[1]).pop()

   # obtaining "g" and 9
   for symbol in six_symbols:
      if num_dict[4].intersection(symbol) == num_dict[4]:
         num_dict[9] = symbol
         letter_mapping["g"] = num_dict[9].difference(num_dict[4]).difference(letter_mapping["a"]).pop()
   six_symbols.remove(num_dict[9])

   # obtaining 0, 6, "c", "e", "d", "f", and "b"
   for symbol in six_symbols:
      if len(num_dict[7].intersection(symbol)) == 3:
         num_dict[0] = symbol
   six_symbols.remove(num_dict[0])
   num_dict[6] = six_symbols.pop()
   letter_mapping["c"] = num_dict[1].difference(num_dict[6]).pop()
   letter_mapping["e"] = num_dict[6].difference(num_dict[9]).pop()
   letter_mapping["d"] = num_dict[4].difference(num_dict[0]).pop()
   letter_mapping["f"] = num_dict[7].difference(set([letter_mapping["a"], letter_mapping["c"]])).pop()
   letter_mapping["b"] = num_dict[4].difference(set([letter_mapping["c"], letter_mapping["d"], letter_mapping["f"]])).pop()

   # obtaining 2, 3, and 5
   num_dict[2] = {letter_mapping["a"], letter_mapping["c"], letter_mapping["d"], letter_mapping["e"], letter_mapping["g"]}
   num_dict[3] = {letter_mapping["a"], letter_mapping["c"], letter_mapping["d"], letter_mapping["f"], letter_mapping["g"]}
   num_dict[5] = {letter_mapping["a"], letter_mapping["b"], letter_mapping["d"], letter_mapping["f"], letter_mapping["g"]}

   return num_dict
   
def decipher_output_value(output_value: List[str], num_dict: DefaultDict[int, Set[str]]) -> int:
   output_value_sets: List[Set[str]] = []
   for val in output_value:
      new_set = set()
      for ch in val:
         new_set.add(ch)
      output_value_sets.append(new_set)

   running_sum = 0
   for val in output_value_sets:
      for k, v in num_dict.items():
         if val == v:
            running_sum = running_sum * 10 + k # Horner's rule

   return running_sum

def sum_all_output_values(signal_patterns: List[List[Set[str]]], output_values: List[List[str]]) -> int:
   running_sum = 0
   
   for index, sig_pattern in enumerate(signal_patterns):
      running_sum += decipher_output_value(output_values[index], create_seven_segment_num_map(sig_pattern))
   
   return running_sum

def main():
   signal_patterns, output_values = parse_input([line.strip() for line in read_lines(FILEPATH)])

   print(f"Part 1 -- {count_easy_digits(output_values)}")
   print(f"Part 2 -- {sum_all_output_values(signal_patterns, output_values)}")

if __name__ == "__main__":
   main()