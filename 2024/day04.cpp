#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day04.txt"
#define XMAS_STR_LEN 4

constexpr char XMAS_CHARS[XMAS_STR_LEN] = {'X', 'M', 'A', 'S'};

const std::vector<std::vector<std::pair<int, int>>> PART1_MOVES =
{
    { {0, -1}, {0, -2}, {0, -3} },      // Horizontal moves <-
    { {0, 1}, {0, 2}, {0, 3} },         // Horizontal moves ->
    { {-1, 0}, {-2, 0}, {-3, 0} },      // Vertical up moves |
    { {1, 0}, {2, 0}, {3, 0} },         // Vertical down moves |
    { {1, 1}, {2, 2}, {3, 3} },         // Diagonal down \ moves
    { {1, -1}, {2, -2}, {3, -3} },      // Diagonal down / moves
    { {-1, 1}, {-2, 2}, {-3, 3} },      // Diagonal up / moves
    { {-1, -1}, {-2, -2}, {-3, -3} },   // Diagonal up \ moves
};

const std::pair<int, int> TOP_LEFT = {-1, -1};
const std::pair<int, int> TOP_RIGHT = {-1, 1};
const std::pair<int, int> BOTTOM_LEFT = {1, -1};
const std::pair<int, int> BOTTOM_RIGHT = {1, 1};

const std::vector<std::pair<int, int>> PART2_MOVES =
{
    TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT
};

int part1(const std::vector<std::vector<char>>& input)
{
    int numXmas = 0;

    for (int row = 0; row < input.size(); row++)
    {
        for (int col = 0; col < input[row].size(); col++)
        {
            if (input[row][col] != 'X') continue;

            for (auto& movesVec : PART1_MOVES)
            {
                int xmasCharIndex = 1;

                for (auto& pair : movesVec)
                {
                    int newRow = row + pair.first;
                    int newCol = col + pair.second;

                    if (!Helpers::isInbounds(input, newRow, newCol))
                        break;
                    
                    if (XMAS_CHARS[xmasCharIndex] != input[newRow][newCol])
                        break;
                    
                    if (xmasCharIndex + 1 == XMAS_STR_LEN)
                    {
                        numXmas++;
                    }
                    xmasCharIndex++;
                }
            }
        }
    }

    return numXmas;
}

int part2(const std::vector<std::vector<char>>& input)
{
    int numCrissCrossXmas = 0;

    for (int row = 0; row < input.size(); row++)
    {
        for (int col = 0; col < input[row].size(); col++)
        {
            if (input[row][col] != 'A') continue;

            // Perform bounds checks first.
            bool outOfBounds = false;
            for (auto& move : PART2_MOVES)
            {
                if (!Helpers::isInbounds(input, row + move.first, col + move.second))
                {
                    outOfBounds = true;
                    break;
                }
            }
            if (outOfBounds) continue;

            // We can check the two diagonals independently.
            // 1. Check M and S going this way "\"
            if (input[row+TOP_LEFT.first][col+TOP_LEFT.second] == 'M'
                && input[row+BOTTOM_RIGHT.first][col+BOTTOM_RIGHT.second] == 'S') {}
            else if (input[row+TOP_LEFT.first][col+TOP_LEFT.second] == 'S'
                && input[row+BOTTOM_RIGHT.first][col+BOTTOM_RIGHT.second] == 'M') {}
            else { continue; }

            // 2. Next, check S and M going this way "/"
            if (input[row+TOP_RIGHT.first][col+TOP_RIGHT.second] == 'M'
                && input[row+BOTTOM_LEFT.first][col+BOTTOM_LEFT.second] == 'S') {}
            else if (input[row+TOP_RIGHT.first][col+TOP_RIGHT.second] == 'S'
                && input[row+BOTTOM_LEFT.first][col+BOTTOM_LEFT.second] == 'M') {}
            else { continue; }

            // If we got here, success!
            numCrissCrossXmas++;
        }    
    }

    return numCrissCrossXmas;
}

int main(void)
{
    std::vector<std::vector<char>> input = FileHelpers::ReadFileIntoListOfLists<char>(FILENAME);

    PART1(part1(input));
    PART2(part2(input));

    return 0;
}