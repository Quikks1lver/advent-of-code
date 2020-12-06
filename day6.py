# 12/6/20

from Helpers.FileHelper import readFileWithLineBreaks
from typing import Dict, List, Set, Tuple, Union
FILEPATH: str = "Input/day6.txt"

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
   
   print(f"Total custom form sum: {count}")
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
   
   print(f"Total common for sum: {sum}")
   return sum

def main():
   customForms: List[str] = readFileWithLineBreaks(FILEPATH)
   
   # Part 1
   calculateFormSumForList(customForms)

   # Part 2
   calculateCommonFormSumForList(customForms)

if __name__ == "__main__":
   main()