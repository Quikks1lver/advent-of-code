#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day02.txt"

bool isValidRow(const std::vector<int>& input)
{
    bool increasing = true;
    bool success = true;
    bool first = true;

    for (int i = 0; i < input.size() - 1; i++)
    {
        int num1 = input[i];
        int num2 = input[i+1];

        if (first)
        {
            first = false;
            if (num2 < num1) increasing = false;
        }
        else
        {
            if (increasing)
            {
                if (num2 < num1)
                {
                    success = false;
                    break;
                }                
            }
            else // decreasing
            {
                if (num2 > num1)
                {
                    success = false;
                    break;
                }
            }
        }


        int diff = std::abs(num2 - num1);
        if (!(diff >= 1 && diff <= 3))
        {
            success = false;
            break;
        }
    }

    return success;
}

std::vector<int> createClonedVectorMinusOneIndex(const std::vector<int>& vec, size_t index)
{
    std::vector<int> newVec = vec;
    newVec.erase(newVec.begin() + index);
    return newVec;
}

int part1(const std::vector<std::vector<int>>& input)
{
    int numValid = 0;
    for (int i = 0; i < input.size(); i++)
    {
        if (isValidRow(input[i]))
            numValid++;
    }
    return numValid;
}

int part2(const std::vector<std::vector<int>>& input)
{
    int numValid = 0;

    for (int i = 0; i < input.size(); i++)
    {
        if (isValidRow(input[i]))
        {
            numValid++;
            continue;
        }

        // Ok, now check if removing each element makes everything work.
        // Terrible runtime, but will work.
        for (int j = 0; j < input[i].size(); j++)
        {
            if (isValidRow(createClonedVectorMinusOneIndex(input[i], j)))
            {
                numValid++;
                break;
            }
        }
    }

    return numValid;
}

int main(void)
{
    std::vector<std::vector<int>> input = FileHelpers::ReadFileIntoListOfLists<int>(FILENAME);

    PART1(part1(input));
    PART2(part2(input));

    return 0;
}