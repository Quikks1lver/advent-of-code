#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day10.txt"

const int TRAILHEAD_START = 0;
const int HIKE_END = 9;

const std::array<std::pair<int, int>, 4> MOVES =
{
    std::pair<int, int>{-1, 0},    // up
    std::pair<int, int>{1, 0},     // down
    std::pair<int, int>{0, -1},    // left
    std::pair<int, int>{0, 1}      // right
};

std::vector<std::pair<int, int>> findTrailHeads(const std::vector<std::vector<int>>& input)
{
    std::vector<std::pair<int, int>> retval;

    for (int row = 0; row < input.size(); row++)
        for (int col = 0; col < input[row].size(); col++)
            if (input[row][col] == TRAILHEAD_START)
                retval.emplace_back(std::pair<int, int>(row, col));
    
    return retval;
}

bool isHikeFailCondition(const std::vector<std::vector<int>>& input, int row, int col, int prevVal)
{
    // Out of bounds, return fail immediately.
    if (!Helpers::isInbounds(input, row, col))
        return true;
    
    int currVal = input[row][col];

    // If this is NaN or diff between values exceeds constraints, return.
    if (currVal == FileHelpers::INVALID_2D_ARR_SPOT)
        return true;
    if (currVal - prevVal != 1)
        return true;

    // Passed all validation thus far.
    return false;
}

// Fills the set with valid hike end positions.
void recursiveHelperPart1(const std::vector<std::vector<int>>& input,
                          std::unordered_set<std::pair<int, int>>& trailEnds,
                          int row,
                          int col,
                          int prevVal)
{
    if (isHikeFailCondition(input, row, col, prevVal))
        return;
    
    // If we're here, we're inbounds and |diff| = 1, so if we've hit a trail end, we've suceeded.
    int currVal = input[row][col];
    if (currVal == HIKE_END)
    {
        trailEnds.insert(std::pair<int, int>(row, col));
        return;
    }

    // If not successful yet, recurse for remaining moves.
    for (const auto& move : MOVES)
        recursiveHelperPart1(input, trailEnds, row + move.first, col + move.second, currVal);
}

int part1(const std::vector<std::vector<int>>& input, const std::vector<std::pair<int, int>>& trailHeads)
{
    int totalTrailHeads = 0;
    for (const auto& trailHead : trailHeads)
    {
        std::unordered_set<std::pair<int, int>> trailEnds;
        int row = trailHead.first;
        int col = trailHead.second;

        for (const auto& move : MOVES)
            recursiveHelperPart1(input, trailEnds, row + move.first, col + move.second, TRAILHEAD_START);
        
        totalTrailHeads += trailEnds.size();
    }
    return totalTrailHeads;
}

// Returns a new string with row, col pair appended to currStr.
string appendCurrMove(const string& currStr, int row, int col)
{
    return currStr + std::to_string(row) + std::to_string(col);
}

// Fills the set with valid hike paths, from trail head -> hike end.
void recursiveHelperPart2(const std::vector<std::vector<int>>& input,
                          std::unordered_set<string>& trailEnds,
                          int row,
                          int col,
                          int prevVal,
                          const string& soFar)
{
    if (isHikeFailCondition(input, row, col, prevVal))
        return;
    
    int currVal = input[row][col];
    if (currVal == HIKE_END)
    {
        trailEnds.insert(soFar);
        return;
    }

    for (const auto& move : MOVES)
    {
        int newRow = row + move.first;
        int newCol = col + move.second;

        // Even though we have checks at top of function, that's a last resort. Let's check OOB
        // and constraint exceeding right now, too, so we can avoid expensive string operations.
        if (isHikeFailCondition(input, newRow, newCol, currVal))
            continue;

        string newStr = appendCurrMove(soFar, newRow, newCol);
        recursiveHelperPart2(input, trailEnds, newRow, newCol, currVal, newStr);
    }
}

int part2(const std::vector<std::vector<int>>& input, const std::vector<std::pair<int, int>>& trailHeads)
{
    int totalTrailRating = 0;
    for (const auto& trailHead : trailHeads)
    {
        int row = trailHead.first;
        int col = trailHead.second;
     
        std::unordered_set<string> trailRatings;

        string currStr = appendCurrMove("", row, col);
        for (const auto& move : MOVES)
        {
            int newRow = row + move.first;
            int newCol = col + move.second;
            string appendedMoveStr = appendCurrMove(currStr, newRow, newCol);

            recursiveHelperPart2(input, trailRatings, newRow, newCol, TRAILHEAD_START, appendedMoveStr);
        }
        
        totalTrailRating += trailRatings.size();
    }
    return totalTrailRating;
}

int main(void)
{
    std::vector<std::vector<int>> input = FileHelpers::Read2DIntArray(FILENAME);
    std::vector<std::pair<int, int>> trailHeads = findTrailHeads(input);

    PART1(part1(input, trailHeads));
    
    // Yes, expensive runtime w/string ops, but first solution I thought of.
    PART2(part2(input, trailHeads));

    return 0;
}