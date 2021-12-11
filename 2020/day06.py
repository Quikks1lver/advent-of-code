# 12/6/20

from Helpers.FileHelper import readFileWithEmptyLineBreaks
from typing import Dict, List, Set, Tuple, Union
FILEPATH: str = "2020/Input/day06.txt"

def calculateFormSum(form: str) -> int:
   """
   Calculates the sum of counts based on the custom form string. Part 1
   """
   formSet: Set[str] = set()

   for letter in form:
      if letter.isalpha():
         formSet.add(letter)
   
   return len(formSet)

def calculateFormSumForList(formList: List[str]) -> int:
   """
   Calculates sum of counts based on custom form string list. Part 1
   """
   count: int = 0

   for form in formList:
      count += calculateFormSum(form)
   
   print(f"Part 1 -- Total custom form sum: {count}")
   return count

def calculateCommonFormSum(form: str) -> int:
   """
   Calculates form sum for questions to which EVERYONE in a group answers yes to. Part 2
   """
   people: List[str] = form.split("\n")
   numPeople: int = len(people)
   peopleAnswersMap: Dict[str] = {}
   sum: int = 0

   for person in people:
      for answer in person:
         if not answer.isspace():
            alreadyThere: Union[int, None] = peopleAnswersMap.get(answer)
            peopleAnswersMap[answer] = 1 if alreadyThere == None else alreadyThere + 1
   
   for numAnswer in peopleAnswersMap.values():
      if numAnswer == numPeople:
         sum += 1
   
   return sum

def calculateCommonFormSumForList(formList: List[str]) -> int:
   """
   Calculates form sum (for a list) for questions to which EVERYONE in a group answers yes to. Part 2
   """
   sum: int = 0

   for form in formList:
      sum += calculateCommonFormSum(form)
   
   print(f"Part 2 -- Total common form sum, only counting shared answers: {sum}")
   return sum

def main():
   customForms: List[str] = readFileWithEmptyLineBreaks(FILEPATH)
   
   # Part 1
   calculateFormSumForList(customForms)

   # Part 2
   calculateCommonFormSumForList(customForms)

if __name__ == "__main__":
   main()

"""
--- Day 6: Custom Customs ---
--- Part One ---
The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify
the questions for which anyone in your group answers "yes". Since your group is just you, this
doesn't take very long.
For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
--- Part Two ---
As you finish the last group's customs declaration, you notice that you misread one word in the instructions:
You don't need to identify the questions to which anyone answered "yes"; you need to identify
the questions to which everyone answered "yes"!
For each group, count the number of questions to which everyone answered "yes".
What is the sum of those counts?
"""