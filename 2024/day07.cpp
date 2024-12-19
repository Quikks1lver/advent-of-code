#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day07.txt"

typedef long long BigNumber;

std::vector<std::pair<BigNumber, std::vector<BigNumber>>> parseRawInput(const std::vector<string>& rawInput)
{
    std::vector<std::pair<BigNumber, std::vector<BigNumber>>> retval;

    for (const string& s : rawInput)
    {
        std::pair<BigNumber, std::vector<BigNumber>> newElement;

        std::istringstream stream(s);

        BigNumber key;
        stream >> key;

        string throwAwayColon;
        stream >> throwAwayColon;

        BigNumber val;
        std::vector<BigNumber> nums;
        while (stream >> val)
            nums.push_back(val);

        newElement.first = key;
        newElement.second = std::move(nums);
        retval.push_back(std::move(newElement));
    }

    return retval;
}

bool isValidRecursiveHelper(BigNumber target,
                            const std::vector<BigNumber>& nums,
                            BigNumber runningVal,
                            int currIndex,
                            bool withConcatOperator)
{
    // If we've exceeded target, return immediately.
    if (runningVal > target) return false;
    
    // If we've reached end of nums, check whether we've hit target.
    if (currIndex == nums.size()) return runningVal == target;

    BigNumber currNum = nums[currIndex];

    if (isValidRecursiveHelper(target, nums, runningVal + currNum, currIndex+1, withConcatOperator)) return true;
    if (isValidRecursiveHelper(target, nums, runningVal * currNum, currIndex+1, withConcatOperator)) return true;
    if (withConcatOperator)
    {
        // I could use Horner's rule or something, but we'll make this easy on ourselves.
        string runningValStr = std::to_string(runningVal);
        string currNumStr = std::to_string(currNum);
        string concatStr = runningValStr + currNumStr;
        if (isValidRecursiveHelper(target, nums, std::stoll(concatStr), currIndex+1, withConcatOperator)) return true;
    }
    return false;
}

bool isValid(const std::pair<BigNumber, std::vector<BigNumber>>& listing, bool withConcatOperator)
{
    return isValidRecursiveHelper(listing.first, listing.second, listing.second.at(0), 1, withConcatOperator);
}

BigNumber part1(std::vector<std::pair<BigNumber, std::vector<BigNumber>>>& mapping)
{
    BigNumber retval = 0;
    for (const std::pair<BigNumber, std::vector<BigNumber>>& pair : mapping)
        retval += (isValid(pair, false)) ? pair.first : 0;
    return retval;
}

BigNumber part2(std::vector<std::pair<BigNumber, std::vector<BigNumber>>>& mapping)
{
    BigNumber retval = 0;
    for (const std::pair<BigNumber, std::vector<BigNumber>>& pair : mapping)
        retval += (isValid(pair, true)) ? pair.first : 0;
    return retval;
}

int main(void)
{
    std::vector<string> rawInput = FileHelpers::ReadFileIntoStrings(FILENAME);
    std::vector<std::pair<BigNumber, std::vector<BigNumber>>> mapping = parseRawInput(rawInput);

    PART1(part1(mapping));
    PART2(part2(mapping));

    return 0;
}
