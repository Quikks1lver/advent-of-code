# --- Day 2: Password Philosophy ---
# suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the 
# lowest and highest number of times a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
# How many passwords are valid according to their policies?

import re
from FileHelper import readFile

FILEPATH: str = "Input/inputTwo.txt"

def componentizePassword(password: str) -> (int, int, str, str):
   """
   Takes a password and converts it into its components (lowerBound, upperBound, targetLetter, password)
   """

   pieces: list = password.rstrip().split(" ")
   bounds: list = pieces[0].split("-")
   targetLetter: str = pieces[1].rstrip(":")
   
   return int(bounds[0]), int(bounds[1]), targetLetter, pieces[-1]

def isValidPassword(lowerBound: int, upperBound: int, targetLetter: str, password: str) -> int:
   """
   Takes a password and returns 1 if valid, 0 otherwise
   """

   validSoFar: bool = True
   letterCount: int = 0
   
   for char in password:
      if char == targetLetter:
         letterCount += 1
      if letterCount > upperBound:
         validSoFar = False
         break
   
   return 1 if validSoFar and letterCount >= lowerBound else 0

def main():
   lines: list = readFile(FILEPATH)
   validPasswords: int = 0

   for line in lines:
      lower, upper, target, password = componentizePassword(line)
      validPasswords += isValidPassword(lower, upper, target, password)
   
   print(f"Number of valid passwords: {validPasswords}")

if __name__ == "__main__":
    main()