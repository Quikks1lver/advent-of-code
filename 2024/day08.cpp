#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day08.txt"

const char NOTHING = '.';

std::unordered_map<char, std::vector<std::pair<int, int>>> createAntennaToCoordsMap(const std::vector<std::vector<char>>& input)
{
    std::unordered_map<char, std::vector<std::pair<int, int>>> retval;

    for (int row = 0; row < input.size(); row++)
    {
        for (int col = 0; col < input[row].size(); col++)
        {
            char ch = input[row][col];
            if (ch == NOTHING) continue;

            std::pair<int, int> coord(row, col);

            if (retval.find(ch) == retval.end())
                retval[ch] = std::vector<std::pair<int, int>>();

            retval[ch].emplace_back(coord); // No need to std::move as this obj is small.
        }
    }

    return retval;
}

int part1(const std::vector<std::vector<char>>& input,
          const std::unordered_map<char, std::vector<std::pair<int, int>>>& antennaToCoordsMap)
{
    std::unordered_set<std::pair<int, int>> antiNodes;

    for (const std::pair<const char, std::vector<std::pair<int, int>>>& keyValPair : antennaToCoordsMap)
    {
        const std::vector<std::pair<int, int>>& vec = keyValPair.second;

        for (int i = 0; i < vec.size() - 1; i++)
        {
            for (int j = i + 1; j < vec.size(); j++)
            {
                const std::pair<int, int>& pair1 = vec[i];
                const std::pair<int, int>& pair2 = vec[j];

                int rowDelta = pair1.first - pair2.first;
                int colDelta = pair1.second - pair2.second;

                std::pair<int, int> antiNode1(pair1.first + rowDelta, pair1.second + colDelta);
                std::pair<int, int> antiNode2(pair2.first - rowDelta, pair2.second - colDelta);

                if (Helpers::isInbounds(input, antiNode1.first, antiNode1.second))
                    antiNodes.insert(antiNode1);
                if (Helpers::isInbounds(input, antiNode2.first, antiNode2.second))
                    antiNodes.insert(antiNode2);
            }
        }
    }

    return antiNodes.size();
}

int part2(const std::vector<std::vector<char>>& input,
          const std::unordered_map<char, std::vector<std::pair<int, int>>>& antennaToCoordsMap)
{
    std::unordered_set<std::pair<int, int>> antiNodes;

    for (const std::pair<const char, std::vector<std::pair<int, int>>>& keyValPair : antennaToCoordsMap)
    {
        const std::vector<std::pair<int, int>>& vec = keyValPair.second;

        for (int i = 0; i < vec.size() - 1; i++)
        {
            for (int j = i + 1; j < vec.size(); j++)
            {
                const std::pair<int, int>& pair1 = vec[i];
                const std::pair<int, int>& pair2 = vec[j];

                // Each pair is also an antinode here.
                antiNodes.insert(pair1);
                antiNodes.insert(pair2);

                int rowDelta = pair1.first - pair2.first;
                int colDelta = pair1.second - pair2.second;

                std::pair<int, int> antiNode1(pair1.first + rowDelta, pair1.second + colDelta);
                std::pair<int, int> antiNode2(pair2.first - rowDelta, pair2.second - colDelta);

                // Keep looping and adding in more antinodes.
                while (Helpers::isInbounds(input, antiNode1.first, antiNode1.second))
                {
                    antiNodes.insert(antiNode1);
                    antiNode1.first += rowDelta;
                    antiNode1.second += colDelta;
                }
                while (Helpers::isInbounds(input, antiNode2.first, antiNode2.second))
                {
                    antiNodes.insert(antiNode2);
                    antiNode2.first -= rowDelta;
                    antiNode2.second -= colDelta;
                }
            }
        }
    }

    return antiNodes.size();
}

int main(void)
{
    std::vector<std::vector<char>> input = FileHelpers::ReadFileIntoListOfLists<char>(FILENAME);
    auto antennaToCoordsMap = createAntennaToCoordsMap(input);

    PART1(part1(input, antennaToCoordsMap));
    PART2(part2(input, antennaToCoordsMap));

    return 0;
}
