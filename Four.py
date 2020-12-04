# 12/4/20

from Helpers.FileHelper import readFile
from typing import List, Tuple
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
            tempPassport = tempPassport.strip()
            passportList.append(tempPassport)
         tempPassport = ""
      else:
         tempPassport += " " + line
   passportList.append(tempPassport) # don't forget last one!

   return passportList

def countValidPassports(passportList: List[str], requirements: Tuple[str]) -> int:
   """
   Counts number of valid passports in a passport list
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

def main():
   passportList: List[str] = createPassportList(FILEPATH)
   requirements: Tuple[str] = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
   validPassports: int = countValidPassports(passportList, requirements)

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
"""