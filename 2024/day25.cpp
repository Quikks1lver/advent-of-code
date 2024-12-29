#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day25.txt"

const string END = "END";

// First holds locks, second keys.
std::pair<std::vector<std::vector<int>>, std::vector<std::vector<int>>> extractLocksAndKeys(std::vector<string>& input)
{
    std::vector<std::vector<int>> locks;
    std::vector<std::vector<int>> keys;
    std::vector<int> tempVec;

    bool newEntity = true;
    bool isLock = true;

    // We're going one over so we can catch last line!
    for (int i = 0; i < input.size() + 1; i++)
    {
        const string& line = (i < input.size()) ? input[i] : END;

        // Empty string, so add to respective vector and reset.
        if (line.empty() || line == END)
        {
            newEntity = true;
            
            if (tempVec.size() > 0)
            {
                if (isLock) locks.push_back(std::move(tempVec));
                else keys.push_back(std::move(tempVec));
            }
            
            tempVec.clear();
        }
        // Determine whether lock or key and initialize temp vec.
        else if (newEntity)
        {
            isLock = line.at(0) == '#';

            // Fill up keys with -1 so we don't double count last row.
            tempVec.insert(tempVec.end(), 5, isLock ? 0 : -1);
            
            newEntity = false;
        }
        // Add to temporary vector.
        else
        {
            for (int i = 0; i < line.size(); i++)
                if (line.at(i) == '#')
                    tempVec[i]++;
        }
    }

    return {locks, keys};
}

int part1(std::vector<std::vector<int>>& locks, std::vector<std::vector<int>>& keys)
{
    int totalSuccesses = 0;
    for (const auto& lock : locks)
    {
        for (const auto& key : keys)
        {
            bool thisLKSuccess = true;
            for (int i = 0; i < 5; i++)
                if (lock[i] + key[i] > 5)
                    thisLKSuccess = false;
            if (thisLKSuccess) totalSuccesses++;    
        }
    }
    return totalSuccesses;
}

int main(void)
{
    std::vector<string> input = FileHelpers::ReadFileIntoStrings(FILENAME);

    auto retval = extractLocksAndKeys(input);
    std::vector<std::vector<int>> locks = std::move(retval.first);
    std::vector<std::vector<int>> keys = std::move(retval.second);

    PART1(part1(locks, keys));
    // I can't complete part 2 as of 12/28/24 since I haven't completed all other puzzles.

    return 0;
}
