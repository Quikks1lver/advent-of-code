#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day06.txt"

const char GUARD_START = '^';
const char OBSTACLE = '#';
const char OK = '.';

std::array<char, 4> NEXT_MOVE = {'^', '>', 'v', '<'};
std::unordered_map<char, std::pair<int, int>> MOVES =
{
    {'^', {-1, 0}},
    {'>', {0, 1}},
    {'<', {0, -1}},
    {'v', {1, 0}},
};

char getNextMoveDirection(char ch)
{
    int pos = -1;
    for (int i = 0; i < NEXT_MOVE.size(); i++)
        if (NEXT_MOVE[i] == ch)
            pos = i;
    
    if (pos == -1)
        throw std::invalid_argument("Invalid move passed in");
    
    return NEXT_MOVE[(pos + 1) % NEXT_MOVE.size()];
}

std::pair<int, int> getCoordsOfStart(const std::vector<std::vector<char>>& input)
{
    for (int row = 0; row < input.size(); row++)
    {
        for (int col = 0; col < input[row].size(); col++)
        {
            if (input[row][col] == GUARD_START)
            {
                return std::pair<int, int>(row, col);
            }
        }
    }

    throw std::invalid_argument("No guard found.");
}

std::pair<int, int> getNextMoveDelta(char ch)
{
    return MOVES.at(ch);
}

int part1(const std::vector<std::vector<char>>& input)
{
    std::pair<int, int> startingPt = getCoordsOfStart(input);
    std::unordered_set<std::pair<int, int>> positionsSet;
    
    int currRow = startingPt.first;
    int currCol = startingPt.second;
    char currGuardDirection = GUARD_START;

    while (true)
    {
        // If we're in the loop, valid position, so mark as visited.
        positionsSet.insert(std::pair<int, int>(currRow, currCol));

        std::pair<int, int> nextDelta = getNextMoveDelta(currGuardDirection);
        char newGuardDirection = currGuardDirection;

        int newRow = currRow + nextDelta.first;
        int newCol = currCol + nextDelta.second;

        if (!Helpers::isInbounds(input, newRow, newCol))
            break;
        
        char charAtNewPos = input[newRow][newCol];

        switch (charAtNewPos)
        {
            case OBSTACLE:
                // We have to reset our newRow and newCol, and instead reorient.
                newRow = currRow;
                newCol = currCol;
                newGuardDirection = getNextMoveDirection(currGuardDirection);
                break;
            
            case OK:
            default:
                // No issue moving forward, so take the step.
                break;
        }
        
        // Reset currRow and currCol.
        currRow = newRow;
        currCol = newCol;
        currGuardDirection = newGuardDirection;
    }

    // Sum up visited cells and return.
    return positionsSet.size();
}

bool isLoop(const std::vector<std::vector<char>>& input, std::pair<int, int> startingPt)
{
    std::unordered_set<std::pair<int, int>> positionsSet;
    int limitBreak = input.size() * input[0].size();
    
    int currRow = startingPt.first;
    int currCol = startingPt.second;
    char currGuardDirection = GUARD_START;
    int numRoundsWithoutAddingNewPosition = 0;

    while (true)
    {
        // If we're in the loop, valid position, so mark as visited.
        int oldSetSize = positionsSet.size();
        positionsSet.insert(std::pair<int, int>(currRow, currCol));
        int newSetSize = positionsSet.size();

        numRoundsWithoutAddingNewPosition = (oldSetSize == newSetSize) ?
                                            numRoundsWithoutAddingNewPosition + 1
                                            : 0;
        
        // This means we've hit a loop.
        if (numRoundsWithoutAddingNewPosition >= limitBreak)
            return true;

        std::pair<int, int> nextDelta = getNextMoveDelta(currGuardDirection);
        char newGuardDirection = currGuardDirection;

        int newRow = currRow + nextDelta.first;
        int newCol = currCol + nextDelta.second;

        if (!Helpers::isInbounds(input, newRow, newCol))
            break;
        
        char charAtNewPos = input[newRow][newCol];

        switch (charAtNewPos)
        {
            case OBSTACLE:
                // We have to reset our newRow and newCol, and instead reorient.
                newRow = currRow;
                newCol = currCol;
                newGuardDirection = getNextMoveDirection(currGuardDirection);
                break;
            
            case OK:
            default:
                // No issue moving forward, so take the step.
                break;
        }
        
        // Reset currRow and currCol.
        currRow = newRow;
        currCol = newCol;
        currGuardDirection = newGuardDirection;
    }

    // This means successfully exited, so no loop.
    return false;
}

int part2(const std::vector<std::vector<char>>& input)
{
    std::pair<int, int> startingPt = getCoordsOfStart(input);
    
    // Create a copy of input so we can tweak it for new obstacles.
    std::vector<std::vector<char>> copy = input;

    int numLoops = 0;
    for (int row = 0; row < copy.size(); row++)
    {
        for (int col = 0; col < copy[row].size(); col++)
        {
            if (copy[row][col] == OK)
            {
                copy[row][col] = OBSTACLE; // Make change
                
                if (isLoop(copy, startingPt)) // Test it
                    numLoops++;
                
                copy[row][col] = OK; // Reset
            }
        }
    }

    return numLoops;
}

int main(void)
{
    std::vector<std::vector<char>> input = FileHelpers::ReadFileIntoListOfLists<char>(FILENAME);

    PART1(part1(input));

    // After seeing some solution ideas on Reddit, a faster way of this is keeping track of the
    // positions + DIRECTION, too, since if we see a duplicate, that means a loop.
    // However, since this way I solved it works, I'm happy and will keep it :)
    cout << "Part 2 takes a bit to run xD ... ~30s on my M1 machine." << endl;
    PART2(part2(input));

    return 0; 
}
