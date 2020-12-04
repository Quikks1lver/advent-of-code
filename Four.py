# 12/4/20

from Helpers.FileHelper import readFile
from typing import List, Tuple, Dict
FILEPATH: str = "Input/inputFour.txt"

def createPassportList(filepath: str) -> List[str]:
   """
   Reads an input batch file and outputs a list of concatenated passports
   """
   inputLines: List[str] = readFile(filepath)
   passportList: List[str] = []

   tempPassport: str = ""
   for line in inputLines:
      if line == "\n":
         if tempPassport != "":
            tempPassport = tempPassport.replace(" ", "\n").strip()
            passportList.append(tempPassport)
         tempPassport = ""
      else:
         tempPassport += " " + line
   passportList.append(tempPassport) # don't forget last one!

   return passportList

def countValidPassports(passportList: List[str], requirements: Tuple[str]) -> int:
   """
   Counts number of valid passports in a passport list. Part 1
   """
   reqCount: int = 0
   validPassports: int = 0

   for passport in passportList:
      reqCount = 0

      for req in requirements:
         if req in passport:
            reqCount += 1
      
      if reqCount == len(requirements):
         validPassports += 1
   
   print(f"Valid passports: {validPassports}")
   return validPassports

def constructPassportDictList(passportList: List[str]) -> List[dict]:
   """
   Constructs a list of dicts of passports with all information for easier lookup later. Part 2
   """
   passportDictList: List[dict] = []
   tempDict: dict = {}

   for passport in passportList:
      tempDict = {}
      for line in passport.split("\n"):
         if line != "\n":
            tempDict[line[0:3]] = line[4:]
      passportDictList.append(tempDict)
   
   return passportDictList
   
def isInt(s: str) -> bool:
   """
   Returns True if a string is an int, False otherwise
   """
   try:
      int(s)
      return True
   except ValueError:
      return False

def countValidPassportsWithTighterSecurity(passportDictList: List[dict], requirements: Tuple[str]) -> int:
   """
   Counts valid passports with tighter security. The requirements are hard coded into the function
   for ease of use and speed :p. Part 2
   """
   validPassports: int = 0

   for passportDict in passportDictList:
      success: bool = True

      for req in requirements:
         if req not in passportDict.keys():
            success = False
            break
         
         if req == "byr":
            if not isInt(passportDict["byr"]):
               success = False
               break

            birthYear: int = int(passportDict["byr"])
            if birthYear < 1920 or birthYear > 2002:
               success = False
               break

         elif req == "iyr":
            if not isInt(passportDict["iyr"]):
               success = False
               break
            
            issueYear: int = int(passportDict["iyr"])
            if issueYear < 2010 or issueYear > 2020:
               success = False
               break
         
         elif req == "eyr":
            if not isInt(passportDict["eyr"]):
               success = False
               break

            expYear: int = int(passportDict["eyr"])
            if expYear < 2020 or expYear > 2030:
               success = False
               break

         elif req == "hgt":
            heightUnit: str = passportDict["hgt"][-2:]
            height: int = 0
            
            if heightUnit == "cm":
               if not isInt(passportDict["hgt"][0:3]):
                  success = False
                  break
               
               height = int(passportDict["hgt"][0:3])
               if height < 150 or height > 193:
                  success = False
                  break

            elif heightUnit == "in":
               if not isInt(passportDict["hgt"][0:2]):
                  success = False
                  break
               
               height = int(passportDict["hgt"][0:2])
               if height < 59 or height > 76:
                  success = False
                  break
            
            else: # not cm or in
               success = False
               break

         elif req == "hcl":
            poundSymbol: str = passportDict["hcl"][0]
            code: str = passportDict["hcl"][1:]

            if poundSymbol != "#" and len(code) != 6:
               success = False
               break
            
            for letter in code:
               validLetters: Tuple[str] = ('a', 'b', 'c', 'd', 'e', 'f')
               if letter not in validLetters and not isInt(letter):
                  success = False
                  break

         elif req == "ecl":
            eyeColors: Tuple[str] = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
            if passportDict["ecl"] not in eyeColors:
               success = False
               break

         else: # pid
            passId = passportDict["pid"]
            if len(passportDict["pid"]) != 9 or not isInt(passId):
               success = False
               break

      if success == True:
         validPassports += 1
      
   print(f"Under tighter security, valid passport count: {validPassports}")
   return validPassports


def main():
   passportList: List[str] = createPassportList(FILEPATH)
   requirements: Tuple[str] = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
   
   # Part 1
   validPassports: int = countValidPassports(passportList, requirements)
   
   # Part 2
   passportDictList: List[dict] = constructPassportDictList(passportList)
   countValidPassportsWithTighterSecurity(passportDictList, requirements)

if __name__ == "__main__":
   main()

"""
--- Day 4: Passport Processing ---
--- Part One ---
The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
Count the number of valid passports - those that have all required fields. 
Treat cid as optional. In your batch file, how many passports are valid?
--- Part Two ---
You can continue to ignore the cid field, but each other field has strict rules about what values
are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according
to the above rules. Here are some example values:
"""