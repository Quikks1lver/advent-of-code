# --- Day 2: Password Philosophy ---
# --- Part One ---
# suppose you have the following list:
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password. The password policy indicates the 
# lowest and highest number of times a given letter must appear for the password to be valid. 
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.
#
# How many passwords are valid according to their policies?
# --- Part Two ---
# While it appears you validated the passwords correctly, they don't seem to be what the Official
# Toboggan Corporate Authentication System is expecting.
# Each policy actually describes two positions in the password, where 1 means the first character, 
# 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept 
# of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences 
# of the letter are irrelevant for the purposes of policy enforcement.
# Given the same example list from above:
# 1-3 a: abcde is valid: position 1 contains a and position 3 does not.
# 1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
# 2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
# How many passwords are valid according to the new interpretation of the policies?

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

def isValidPasswordPartOne(lowerBound: int, upperBound: int, targetLetter: str, password: str) -> int:
   """
   Takes a password and returns 1 if valid, 0 otherwise. First part of the puzzle
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

def isValidPasswordPartTwo(firstIndex: int, secondIndex: int, targetLetter: str, password: str) -> int:
   """
   Takes a password and returns 1 if valid, 0 otherwise. Second part of the puzzle
   """
   bool1: bool = password[firstIndex - 1] == targetLetter
   bool2: bool = password[secondIndex - 1] == targetLetter
   return 1 if bool1 ^ bool2 else 0


def main():
   lines: list = readFile(FILEPATH)
   validPasswordsOne: int = 0
   validPasswordsTwo: int = 0

   for line in lines:
      lower, upper, target, password = componentizePassword(line)
      validPasswordsOne += isValidPasswordPartOne(lower, upper, target, password)
      validPasswordsTwo += isValidPasswordPartTwo(lower, upper, target, password)
   
   print(f"Number of valid passwords for part 1: {validPasswordsOne}")
   print(f"Number of valid passwords for part 2: {validPasswordsTwo}")

if __name__ == "__main__":
    main()