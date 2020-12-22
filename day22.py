# 12/22/20

from Helpers.FileHelper import readFileWithEmptyLineBreaks
from typing import List, Union, Set
FILEPATH: str = "Input/day22.txt"

class Player:
   """
   Player of the game Combat
   """
   def __init__(self, name: str, deck: List[int]):
      self.name = name
      self.deck = deck.copy()
   
   def throwDownCard(self) -> int:
      """
      Returns first card in deck and removes card from top of hand
      """
      return self.deck.pop(0)
   
   def wonHand(self, cards: List[int]) -> None:
      """
      Adds cards to back of deck
      """
      for c in cards:
         self.deck.append(c)
   
   def calculateScore(self) -> int:
      """
      Calculates a player's score
      """
      count, score = 1, 0
      for i in range(len(self.deck) - 1, -1, -1):
         score += self.deck[i] * count
         count += 1
      return score

   def __repr__(self):
      return f"{self.name} -- {self.deck}"

def splitDecks(inputLines: List[str]) -> (List[int], List[int]):
   """
   Splits decks up into player 1 and player 2
   """
   deckOne: List[int] = [int(s.strip()) for s in inputLines[0][inputLines[0].index(":") + 2:].split("\n")]
   deckTwo: List[int] = [int(s.strip()) for s in inputLines[1][inputLines[1].index(":") + 2:].split("\n")]
   return deckOne, deckTwo

def determineWinner(playerOne: Player, playerTwo: Player, numRounds: int, printWinner: bool) -> Union[None, Player]:
   """
   Determines winner after a game of Combat (or none if unfinished game) and prints winner, if wanted
   """
   # game is not over
   if len(playerOne.deck) != 0 and len(playerTwo.deck) != 0:
      return None

   winner: Player = playerOne if len(playerOne.deck) != 0 else playerTwo
   if printWinner:
      print(f"After {numRounds} rounds, winner is: {winner}")
   
   return winner

def playCombat(playerOne: Player, playerTwo: Player, printWinner: bool) -> int:
   """
   Plays the game of combat and optionally prints which player wins; returns an int representing who won (1|2)
   WARNING: mutates decks
   """
   numRounds: int = 0

   while len(playerOne.deck) != 0 and len(playerTwo.deck) != 0:
      wonCards: List[int] = []
      numOne = playerOne.throwDownCard()
      numTwo = playerTwo.throwDownCard()
      wonCards.append(numOne)
      wonCards.append(numTwo)
      wonCards.sort(reverse=True)

      if numOne > numTwo:
         playerOne.wonHand(wonCards)
      else:
         playerTwo.wonHand(wonCards)
      
      numRounds += 1

   winner = determineWinner(playerOne, playerTwo, numRounds, printWinner)
   retVal: int = 1 if winner == playerOne else 2
   return retVal

def shouldRecurse(playerOne: Player, playerTwo: Player, cardOne: int, cardTwo: int) -> bool:
   """
   Determines whether the recursive combat game should recurse or not
   """
   if len(playerOne.deck) >= cardOne and len(playerTwo.deck) >= cardTwo:
      return True
   return False

def playRecursiveCombat(playerOne: Player, playerTwo: Player, printWinner: bool) -> int:
   """
   Plays the game of RECURSIVE combat and optionally prints which player wins; returns an int
   representing who won (1|2). WARNING: mutates decks
   """
   numRounds: int = 0
   prevDecks: Set[str] = set()
   recursed: bool = False

   while len(playerOne.deck) > 0 and len(playerTwo.deck) > 0:
      # prevents infinite recursion
      setVal: str = str(playerOne.deck) + str(playerTwo.deck)
      if setVal in prevDecks:
         recursed = True
         break
      prevDecks.add(setVal)
   
      wonCards: List[int] = []
      numOne = playerOne.throwDownCard()
      numTwo = playerTwo.throwDownCard()

      # recurse
      if shouldRecurse(playerOne, playerTwo, numOne, numTwo):
         tempPlayerOne: Player = Player(f"one, recursive", playerOne.deck[0 : numOne])
         tempPlayerTwo: Player = Player(f"two, recursive", playerTwo.deck[0 : numTwo])

         recursiveRoundWinner = playRecursiveCombat(tempPlayerOne, tempPlayerTwo, printWinner)

         if recursiveRoundWinner == 1:
            wonCards.append(numOne)
            wonCards.append(numTwo)
            playerOne.wonHand(wonCards)
         else:
            wonCards.append(numTwo)
            wonCards.append(numOne)
            playerTwo.wonHand(wonCards)
               
      # don't recurse
      else:
         wonCards.append(numOne)
         wonCards.append(numTwo)
         wonCards.sort(reverse=True)

         if numOne > numTwo:
            playerOne.wonHand(wonCards)
         else:
            playerTwo.wonHand(wonCards)
      
      numRounds += 1

   if recursed:
      return 1

   winner = determineWinner(playerOne, playerTwo, numRounds, printWinner)
   retVal: int = 1 if winner == playerOne else 2
   return retVal

def main():
   inputLines: List[str] = readFileWithEmptyLineBreaks(FILEPATH)
   
   deckOne, deckTwo = splitDecks(inputLines)
   playerOne, playerTwo = Player("one", deckOne), Player("two", deckTwo)
   
   # Part 1
   winner: int = playCombat(playerOne, playerTwo, False)
   winningScore: int = playerOne.calculateScore() if winner == 1 else playerTwo.calculateScore()
   print(f"Part 1 -- Player {winner}'s Winning Score (normal combat): {winningScore}")

   # Part 2
   playerOne, playerTwo = Player("one", deckOne), Player("two", deckTwo) # resets players
   print("... takes ~30-45 seconds due to recursion")
   
   winner = playRecursiveCombat(playerOne, playerTwo, False)
   winningScore: int = playerOne.calculateScore() if winner == 1 else playerTwo.calculateScore()
   print(f"Part 2 -- Player {winner}'s Winning Score (recursive combat): {winningScore}")

if __name__ == "__main__":
   main()

"""
--- Day 22: Crab Combat ---
--- Part One ---
It only takes a few hours of sailing the ocean on a raft for boredom to sink in. Fortunately, you brought
a small deck of space cards! You'd like to play a game of Combat, and there's even an opponent available:
a small crab that climbed aboard your raft before you left.
Before the game starts, split the cards so each player has their own deck (your puzzle input). Then,
the game consists of a series of rounds: both players draw their top card, and the player with the
higher-valued card wins the round. The winner keeps both cards, placing them on the bottom of their
own deck so that the winner's card is above the other card. If this causes a player to have all of the
cards, they win, and the game ends.
Once the game ends, you can calculate the winning player's score. The bottom card in their deck is worth
the value of the card multiplied by 1, the second-from-the-bottom card is worth the value of the card
multiplied by 2, and so on. With 10 cards, the top card is worth the value on the card multiplied by 10.
Play the small crab in a game of Combat using the two decks you just dealt. What is the winning player's score?
--- Part Two ---
You lost to the small crab! Fortunately, crabs aren't very good at recursion. To defend your honor as
a Raft Captain, you challenge the small crab to a game of Recursive Combat.
Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair).
Then, the game consists of a series of rounds with a few changes:
    - Before either player deals a card, if there was a previous round in this game that had exactly
      the same cards in the same order in the same players' decks, the game instantly ends in a win
      for player 1. Previous rounds from other games are not considered. (This prevents infinite games
      of Recursive Combat, which everyone agrees is a bad idea.)
    - Otherwise, this round's cards must be in a new configuration; the players begin the round by each
      drawing the top card of their deck as normal. 
    - If both players have at least as many cards remaining in their deck as the value of the card they
      just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
    - Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner
      of the round is the player with the higher-value card.
As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes
the two cards dealt at the beginning of the round and places them on the bottom of their own deck (again
so that the winner's card is above the other card). Note that the winner's card might be the lower-valued
of the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round
causes a player to have all of the cards, they win, and the game ends.
After the game, the winning player's score is calculated from the cards they have in their original deck using
the same rules as regular Combat.
Defend your honor as Raft Captain by playing the small crab in a game of Recursive Combat using the same
two decks as before. What is the winning player's score?
"""