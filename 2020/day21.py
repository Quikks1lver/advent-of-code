# 12/21/20

from Helpers.FileHelper import readFile
from typing import Dict, List, Set
FILEPATH: str = "2020/Input/day21.txt"

def parseAllergenAssociations(inputLines: List[str]) -> (Dict[str, List[str]], List[str]):
   """
   Parses input lines and determines a preliminary mapping of possible allergens,
   also returns a giant list of all ingredients
   """
   prelimAllergenMap: Dict[str, List[str]] = dict()
   allIngredients: List[List[str]] = []

   for line in inputLines:
      ingredients: List[str] = [s for s in line[0 : line.index("(") - 1].split(" ")]
      allergens: List[str] = [s for s in line[line.index("(") + len("contains ") + 1 : line.index(")")].split(", ")]
      allIngredients.append(ingredients)
      
      # loop over each allergen at the end of each line
      for allergen in allergens:
         # if the allergen has been seen before, loop through each ingredient from the line
         # and see if it is NOT a possible ingredient -- remove if so to reduce possibilities
         if allergen in prelimAllergenMap:
            possibleIngredients: List[str] = prelimAllergenMap[allergen]

            for i in range(len(possibleIngredients) - 1, -1, -1):
               if possibleIngredients[i] not in ingredients:
                  possibleIngredients.pop(i)
         
         # if the allergen has not been seen before, simply add all of the possible ingredients to it
         else:
            prelimAllergenMap[allergen] = ingredients.copy()
   
   giantIngredientsList: List[str] = []
   for listOfIngredients in allIngredients:
      for i in listOfIngredients:
         giantIngredientsList.append(i)

   return prelimAllergenMap, giantIngredientsList

def finalizeAllergenMap(prelimAllergyMap: Dict[str, List[str]]) -> Dict[str, str]:
   """
   Takes in the preliminary allergen map and finalizes it, with a 1:1 correspondence
   """
   prelimMap: Dict[str, List[str]] = prelimAllergyMap.copy()
   finalMap: Dict[str, List[str]] = dict()
   foundIngredients: Set[str] = set()

   keepGoing: bool = True
   while keepGoing:
      keepGoing = False

      for allergy, possibleIngredients in prelimMap.items():
         if allergy not in finalMap:
            keepGoing = True
            if len(possibleIngredients) == 1:
               finalMap[allergy] = possibleIngredients[0]
               foundIngredients.add(possibleIngredients[0])
            
            else:
               for i in range(len(possibleIngredients) - 1, -1, -1):
                  if possibleIngredients[i] in foundIngredients:
                     possibleIngredients.pop(i)
   
   return finalMap

def countNumNonAllergenIngredients(finalAllergenMap: Dict[str, str], allIngredients: List[str]) -> int:
   """
   Filters allIngredients down to only ingredients w/o allergens and returns length of said list
   """
   nonAllergenIngredients: List[str] = allIngredients.copy()

   for i in range(len(nonAllergenIngredients) - 1, -1, -1):
         if nonAllergenIngredients[i] in finalAllergenMap.values():
            nonAllergenIngredients.pop(i)
   
   return len(nonAllergenIngredients)

def constructCanonicalDangerousIngredients(finalAllergenMap: Dict[str, str]) -> str:
   """
   Arranges ingredients alphabetically by allergen and outputs the danger string
   """
   allergens: List[str] = [a for a in finalAllergenMap.keys()]
   allergens.sort()

   dangerousIngredients: str = ""
   for a in allergens:
      dangerousIngredients += finalAllergenMap[a] + ","
   
   return dangerousIngredients[0:-1] # leave off trailing comma

def main():
   # I was admittedly confused by the wording of this puzzle, so I watched this helpful video
   # to help me understand what was being asked: https://www.youtube.com/watch?v=tXwh0y0PyPw.
   # Credits to TurkeyDev YouTube for his helpful video and advice.
   
   inputLines: List[str] = [s.strip() for s in readFile(FILEPATH)]

   # Part 1
   prelimAllergenMap, allIngredients = parseAllergenAssociations(inputLines)
   finalMap: Dict[str, str] = finalizeAllergenMap(prelimAllergenMap)
   print(f"Part 1 -- Number of Non-Allergen Ingredients: {countNumNonAllergenIngredients(finalMap, allIngredients)}")

   # Part 2
   print(f"Part 2 -- Canonical Dangerous Ingredients List: {constructCanonicalDangerousIngredients(finalMap)}")

if __name__ == "__main__":
   main()

"""
--- Day 21: Allergen Assessment ---
--- Part One ---
You reach the train's last stop and the closest you can get to your vacation island without getting wet.
There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few
days' worth of food for your journey.
You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that
food's ingredients list followed by some or all of the allergens the food contains.
Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen.
Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an
ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding
ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen
could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.
The first step is to determine which ingredients can't possibly contain any of the allergens in any food
in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an
allergen. Counting the number of times any of these ingredients appear in any ingredients list produces
5: they all appear once each except sbzzf, which appears twice.
Determine which ingredients cannot possibly contain any of the allergens in your list. How many times
do any of those ingredients appear?
--- Part Two ---
Now that you've isolated the inert ingredients, you should have enough information to figure out which
ingredient contains which allergen.
Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your
canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous
ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.
Time to stock your raft with supplies. What is your canonical dangerous ingredient list?
"""