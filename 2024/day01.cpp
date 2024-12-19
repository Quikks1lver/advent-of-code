#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"
#define FILENAME "Input/day01.txt"

class NumberList
{
public:
    NumberList(std::vector<string>& input)
    {
        for (std::vector<string>::iterator it = input.begin(); it != input.end(); it++)
        {
            string s = *it;
            
            int first, second;
            std::istringstream stream(s);
            
            stream >> first >> second;
            list1.push_back(first);
            list2.push_back(second);
        }
    }

    std::vector<int> list1;
    std::vector<int> list2;
};

int part1(const NumberList& nList)
{
    int sum = 0;
    for (int i = 0, j = 0; i < nList.list1.size(); i++, j++)
    {
        sum += std::abs(nList.list1[i] - nList.list2[j]);
    }

    return sum;
}

int part2(const NumberList& nList)
{
    // Construct hash map of right hand side.
    std::unordered_map<int, int> map;
    
    int j = 0;
    while (j < nList.list2.size())
    {
        int numInstances = 0;
        int num = nList.list2[j];

        while (j < nList.list2.size() && nList.list2[j] == num)
        {
            numInstances++;
            j++;
        }

        map[num] = numInstances;
    }
    
    int similarity = 0;
    int i = 0;

    while (i < nList.list1.size())
    {
        int newNum = nList.list1[i];
        int leftInstances = 0;
        int rightInstances = 0;

        // No matter what, increment until we're done seeing this number.
        while (i < nList.list1.size() && nList.list1[i] == newNum)
        {
            leftInstances++;
            i++;
        }

        // Now, check if there's a corresponding amount in other side.
        std::unordered_map<int, int>::iterator val = map.find(newNum);
        if (val != map.end())
        {
            rightInstances = val->second;
        }

        if (rightInstances == 0) continue;

        similarity += leftInstances * newNum * rightInstances;
    }

    return similarity;
}

int main(void)
{
    std::vector<string> input = FileHelpers::ReadFileIntoStrings(FILENAME);

    NumberList numberList(input);
    std::sort(numberList.list1.begin(), numberList.list1.end());
    std::sort(numberList.list2.begin(), numberList.list2.end());
    
    PART1(part1(numberList));
    PART2(part2(numberList));

    return 0;
}