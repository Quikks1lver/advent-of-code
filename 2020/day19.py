# 12/19/20

from Helpers.AOC import whiteFlag
from Helpers.FileHelper import readFile
from typing import Dict, List
FILEPATH: str = "2020/Input/day19.txt"

def constructRulesMap(rawRules: List[int]) -> Dict[int, List[int]]:
   """
   Constructs a dict/map from raw rules
   """
   # To be continued . . .

def isValidString(rulesMap: Dict[int, List[int]], startProduction: int, message: str) -> bool:
   """
   Performs a reverse derivation to see if the message is valid in the grammar, from starting production
   """
   # To be continued . . .

def main():
   fullInput: List[str] = readFile(FILEPATH)
   
   rules: List[str] = [s.strip() for s in fullInput[0 : fullInput.index("\n")]]
   messages: List[str] = [s.strip() for s in fullInput[fullInput.index("\n") + 1:]]

   # Part 1
   whiteFlag(1, "Num valid strings", "12/19")
   
   # Part 2
   whiteFlag(2, "?", "12/19")

if __name__ == "__main__":
   main()

"""
--- Day 19: Monster Messages ---
--- Part One ---
They sent you a list of the rules valid messages should obey and a list of received messages they've
collected so far (your puzzle input).
The rules for valid messages (the top part of your puzzle input) are numbered and build upon each other. For example:
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
Your goal is to determine the number of messages that completely match rule 0. In the above example,
ababbb and abbbab match, but bababa, aaabbb, and aaaabbb do not, producing the answer 2. The whole
message must match all of rule 0; there can't be extra unmatched characters in the message. (For
example, aaaabbb might appear to match rule 0 above, but it has an extra unmatched b on the end.)
--- Part Two ---
"""