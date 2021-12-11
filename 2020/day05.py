# 12/5/20

from Helpers.Binary import convertBinaryToDecimal
from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "2020/Input/day05.txt"

def createTicketList(filename:str) -> List[str]:
   """
   Returns a list of tickets from a file
   """
   return [line.strip() for line in readFile(filename)]

def calculateTicketID(ticket: str) -> int:
   """
   Calculates ID for a ticket
   """
   ticket = ticket.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")

   row: int = convertBinaryToDecimal(ticket[0:7])
   col: int = convertBinaryToDecimal(ticket[7:])

   return (row * 8) + col

def findHighestTicket(ticketList: List[str]) -> int:
   """
   Finds and returns the ticket which has the highest seat ID. Part 1
   """
   max: int = 0
   
   for ticket in ticketList:
      tempID = calculateTicketID(ticket)

      if tempID > max:
         max = tempID
   
   print(f"Max ID: {max}")
   return max

def findMissingTicket(ticketList: List[str]) -> int:
   """
   Finds the missing ticket ID from the list. Part 2
   """
   ticketIDList: List[int] = [calculateTicketID(t) for t in ticketList]
   ticketIDList.sort()
   target: int = 0

   for i in range(len(ticketIDList) - 1):
      if ticketIDList[i + 1] != ticketIDList[i] + 1:
         target = ticketIDList[i] + 1
         break

   print(f"Your ticket, the missing one, has ID: {target}")
   return target

def main():
   ticketList: List[str] = createTicketList(FILEPATH)
   
   # Part 1
   findHighestTicket(ticketList)

   # Part 2
   findMissingTicket(ticketList)

if __name__ == "__main__":
   main()

"""
--- Day 5: Binary Boarding ---
--- Part One ---
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane
(numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with
the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the
back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until
you're left with exactly one row.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
--- Part Two ---
It's a completely full flight, so your seat should be the only missing boarding pass in your list.
However, there's a catch: some of the seats at the very front and back of the plane don't
exist on this aircraft, so they'll be missing from your list as well.
Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from
yours will be in your list.
What is the ID of your seat?
"""