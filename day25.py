# 12/25/20

from Helpers.FileHelper import readFile
from typing import List
FILEPATH: str = "Input/day25.txt"

def calculateLoopSize(key: int) -> int:
   val: int = 1
   subjectNumber: int = 7
   numLoops: int = 0

   while val != key:
      val *= subjectNumber
      val %= 20201227
      numLoops += 1
   
   return numLoops

def calculateEncryptionKey(subjectNumber: int, numLoops: int) -> int:
   """
   Calculates encryption key
   """
   val: int = 1

   for _ in range(numLoops):
      val *= subjectNumber
      val %= 20201227
   
   return val

def main():
   inputLines: List[str] = [s.strip() for s in readFile(FILEPATH)]
   cardPublicKey, doorPublicKey = int(inputLines[0]), int(inputLines[1])

   # Part 1
   # This operation takes ~2 minutes, so I ran the code and hand put the values in below
   # cardLoops: int = calculateLoopSize(cardPublicKey)
   # doorLoops: int = calculateLoopSize(doorPublicKey)
   cardLoops: int = 8987376
   doorLoops: int = 14382089
   print(f"Part 1 -- Encryption Key: {calculateEncryptionKey(cardPublicKey, doorLoops)}")

   # No part 2 xD

if __name__ == "__main__":
   main()

"""
--- Day 25: Combo Breaker ---
--- Part One ---
The card always uses a specific, secret loop size when it transforms a subject number. The door always
uses a different, secret loop size.
The cryptographic handshake works like this:
    The card transforms the subject number of 7 according to the card's secret loop size. The result is called the card's public key.
    The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.
    The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device. Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, you have both public keys, but neither device's loop size.
    The card transforms the subject number of the door's public key according to the card's loop size. The result is the encryption key.
    The door transforms the subject number of the card's public key according to the door's loop size. The result is the same encryption key as the card calculated.
If you can use the two public keys to determine each device's loop size, you will have enough information
to calculate the secret encryption key that the card and door use to communicate; this would let you
send the unlock command directly to the door!
What encryption key is the handshake trying to establish?
--- Part Two ---
The light turns green and the door unlocks. As you collapse onto the bed in your room, your pager goes off!
"It's an emergency!" the Elf calling you explains. "The soft serve machine in the cafeteria on sub-basement
7 just failed and you're the only one that knows how to fix it! We've already dispatched a reindeer to
your location to pick you up."
You hear the sound of hooves landing on your balcony.
The reindeer carefully explores the contents of your room while you figure out how you're going to pay
the 50 stars you owe the resort before you leave. Noticing that you look concerned, the reindeer wanders
over to you; you see that it's carrying a small pouch.
"Sorry for the trouble," a note in the pouch reads. Sitting at the bottom of the pouch is a gold coin
with a little picture of a starfish on it.
Looks like you only needed 49 stars after all. =)
"""