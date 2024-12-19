from Helpers.FileHelpers import read_lines
from typing import List, Tuple
FILEPATH = "2022/Input/day02.txt"

WIN = 6
TIE = 3
LOSS = 0

ROCK = 'A'
PAPER = 'B'
SCISSORS = 'C'

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

def play_normally(input: List[Tuple[str]]) -> int:
    YOUR_ROCK = 'X'
    YOUR_PAPER = 'Y'
    YOUR_SCISSORS = 'Z'

    score = 0
    for opponent, you in input:
        if opponent == ROCK:
            if you == YOUR_PAPER: score += WIN
            elif you == YOUR_ROCK: score += TIE
        elif opponent == PAPER:
            if you == YOUR_SCISSORS: score += WIN
            elif you == YOUR_PAPER: score += TIE
        else:
            if you == YOUR_ROCK: score += WIN
            elif you == YOUR_SCISSORS: score += TIE
        
        if you == YOUR_ROCK: score += ROCK_SCORE
        elif you == YOUR_PAPER: score += PAPER_SCORE
        else: score += SCISSORS_SCORE
    
    return score

def play_smartly(input: List[Tuple[str]]) -> int:
    YOU_LOSE = 'X'
    YOU_TIE = 'Y'
    YOU_WIN = 'Z'

    score = 0
    for opponent, you in input:
        if opponent == ROCK:
            if you == YOU_LOSE: score += SCISSORS_SCORE
            elif you == YOU_WIN: score += PAPER_SCORE
            else: score += ROCK_SCORE
        elif opponent == PAPER:
            if you == YOU_LOSE: score += ROCK_SCORE
            elif you == YOU_WIN: score += SCISSORS_SCORE
            else: score += PAPER_SCORE
        else:
            if you == YOU_LOSE: score += PAPER_SCORE
            elif you == YOU_WIN: score += ROCK_SCORE
            else: score += SCISSORS_SCORE

        if you == YOU_WIN: score += WIN
        elif you == YOU_TIE: score += TIE

    return score    

def main():
   input: List[Tuple[str]] = [tuple(line.strip().split(' ')) for line in read_lines(FILEPATH)]

   print(f"Part 1 -- {play_normally(input)}")
   print(f"Part 2 -- {play_smartly(input)}")

if __name__ == "__main__": main()