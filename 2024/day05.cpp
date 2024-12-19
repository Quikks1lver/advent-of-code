#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day05.txt"

bool isCorrectlyOrdered(std::vector<int>& row, std::unordered_map<int, std::unordered_set<int>>& numToNumsAfterMap)
{
    for (int i = row.size() - 1; i >= 1; i--) // Skip 0th element b/c of inner loop.
    {
        int currentNum = row[i];
        
        // This number isn't in the map, so continue on.
        auto it = numToNumsAfterMap.find(currentNum);
        if (it == numToNumsAfterMap.end())
            continue;
        
        std::unordered_set<int> setOfNums = it->second;
        for (int j = i - 1; j >= 0; j--)
        {
            if (setOfNums.find(row[j]) != setOfNums.end())
            {
                // Yikes! Remember this set is numbers that should occur after number we're
                // looking at. Since we're going from backwards -> forwards, if we see a number
                // ahead of us, it's chalked!
                return false;
            }
        }
    }

    return true;
}

int getMiddleNumber(std::vector<int>& vec)
{
    return vec[vec.size() / 2];
}

// We need this instead of using set_intersection b/c that STL function expects an ordered set
// and we're not using one.
std::unordered_set<int> setIntersection(const std::unordered_set<int>& set1, 
                                        const std::unordered_set<int>& set2)
{
    std::unordered_set<int> res;

    for (const int& val : set1)
        if (set2.find(val) != set2.end())
            res.insert(val);

    return res;
}

int part1(std::unordered_map<int, std::unordered_set<int>>& numToNumsAfterMap, std::vector<std::vector<int>>& rows)
{
    int retval = 0;

    for (std::vector<int>& row : rows)
        if (isCorrectlyOrdered(row, numToNumsAfterMap))
            retval += getMiddleNumber(row);

    return retval;
}

int part2(std::unordered_map<int, std::unordered_set<int>>& numsToNumsBeforeMap,
          std::unordered_map<int, std::unordered_set<int>>& numsToNumsAfterMap,
          std::vector<std::vector<int>>& rows)
{
    int retval = 0;

    for (std::vector<int>& row : rows)
    {
        // If we're correctly ordered already, skip this row.
        if (isCorrectlyOrdered(row, numsToNumsAfterMap))
            continue;

        // Construct new mapping for this row.
        std::unordered_map<int, std::unordered_set<int>> currNumsToNumsBeforeMap;
        std::unordered_set<int> numsInRow(row.begin(), row.end());
        for (int val : row)
        {
            // Creates a copy of the set in here.
            if (numsToNumsBeforeMap.find(val) == numsToNumsBeforeMap.end())
            {
                currNumsToNumsBeforeMap[val] = std::unordered_set<int>();
                continue;
            }

            std::unordered_set<int> dependencies = numsToNumsBeforeMap.at(val);
            currNumsToNumsBeforeMap[val] = setIntersection(dependencies, numsInRow);
        }

        // Now, perform a toposort!
        std::vector<int> newRow;

        while (currNumsToNumsBeforeMap.size() > 0)
        {
            int poppedVal;

            // Find newest num that's been 'unlocked'.
            for (const auto& pair : currNumsToNumsBeforeMap)
            {
                std::unordered_set<int> set = pair.second;
                if (set.size() == 0)
                {
                    poppedVal = pair.first;
                    break;
                }
            }

            // Remove that from the mapping.
            currNumsToNumsBeforeMap.erase(poppedVal);

            // Update every other key:value pair in the mapping to remove that dependency.
            for (auto& pair : currNumsToNumsBeforeMap)
            {
                // We need a REFERENCE to the pair.second, else, default C++ behavior when
                // grabbing a container is giving a copy. Alternatively, we could directly modify
                // pair.second via pair.second.erase(...)
                std::unordered_set<int>& set = pair.second;
                set.erase(poppedVal);
            }

            newRow.push_back(poppedVal);
        }

        retval += getMiddleNumber(newRow);
    }

    return retval;
}

int main(void)
{
    auto input = FileHelpers::ReadFileIntoStrings(FILENAME);

    // Parse input for parts 1 and 2.
    // Part 1: map of number : numbers that go after it.
    // Part 2: map of number : numbers that go before it.
    std::unordered_map<int, std::unordered_set<int>> numToNumsAfterMap;
    std::unordered_map<int, std::unordered_set<int>> numToNumsBeforeMap;
    std::vector<std::vector<int>> rows;
    std::regex pattern(R"((\d+)\|(\d+))");
    
    for (string& s : input)
    {
        std::smatch match;

        if (std::regex_search(s, match, pattern)) // First portion of input
        {
            int key = stoi(match[1]);
            int val = stoi(match[2]);
            numToNumsAfterMap[key].insert(val);
            numToNumsBeforeMap[val].insert(key);
        }
        else if (s.size() <= 1)
        {
            // Whitespace, pass.
        }
        else // Row by row raw input now.
        {
            std::vector<int> newRow;

            std::istringstream stream(s);
            string token;

            while (std::getline(stream, token, ','))
            {
                // Convert each token to an integer and add to the vector
                newRow.push_back(std::stoi(token));
            }

            rows.push_back(std::move(newRow));
        }
    }

    PART1(part1(numToNumsAfterMap, rows));
    PART2(part2(numToNumsBeforeMap, numToNumsAfterMap, rows));

    return 0; 
}
