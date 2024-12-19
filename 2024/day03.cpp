#include "Helpers/FileHelpers.h"
#include "CommonIncludes.h"

#define FILENAME "Input/day03.txt"

int calculateMultsForAString(const string& input)
{
    int retval = 0;

    std::regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
    auto begin = std::sregex_iterator(input.begin(), input.end(), pattern);
    auto end = std::sregex_iterator(); // defaults to end iterator

    for (auto it = begin; it != end; it++)
    {
        int num1 = std::stoi(it->str(1));
        int num2 = std::stoi(it->str(2));
        retval += num1 * num2;
    }

    return retval;
}

int part1(const std::vector<string>& input)
{
    int retval = 0;

    for (const string& s : input)
        retval += calculateMultsForAString(s);

    return retval;
}

int part2(const std::vector<string>& input)
{
    int retval = 0;
    bool go = true;

    std::string doString("do()");
    std::string dontString("don't()");

    std::regex dontPattern(R"(don't\(\))"); // don't()
    std::regex doPattern(R"(do\(\))"); // do()

    for (const string& s : input)
    {
        int startIndex = 0;
        int endIndex = s.size();
        
        while (true)
        {
            // Look for both do and dont patterns
            std::smatch doMatch;
            bool doSuccess = std::regex_search(s.begin() + startIndex, s.end(), doMatch, doPattern);

            std::smatch dontMatch;
            bool dontSuccess = std::regex_search(s.begin() + startIndex, s.end(), dontMatch, dontPattern);

            // We have 4 cases to consider.
            // 1. We see neither match ahead of us, so process the rest of the string and break out.
            if (!doSuccess && !dontSuccess)
            {
                // No more conditionals rest of this string, so determine whether to pass this string on.
                if (go)
                    retval += calculateMultsForAString(s.substr(startIndex, string::npos));
                break;
            }

            // 2. We see both matches. Determine which is seen first, then process that substring.
            else if (doSuccess && dontSuccess)
            {
                // match object position field gives offset from the start iterator
                int doEndIndex = startIndex + doMatch.position(0);
                int dontEndIndex = startIndex + dontMatch.position(0);

                if (doEndIndex < dontEndIndex)
                {
                    endIndex = doEndIndex + doString.size();
                    int length = endIndex - startIndex + 1;

                    if (go)
                        retval += calculateMultsForAString(s.substr(startIndex, length));

                    startIndex = endIndex;
                    go = true;
                }
                else
                {
                    endIndex = dontEndIndex + dontString.size();
                    int length = endIndex - startIndex + 1;

                    if (go)
                        retval += calculateMultsForAString(s.substr(startIndex, length));

                    startIndex = endIndex;

                    go = false;
                }
            }

            // 3. We only see the do() match.
            else if (doSuccess)
            {
                endIndex = startIndex + doMatch.position(0) + doString.size();
                int length = endIndex - startIndex + 1;

                if (go)
                    retval += calculateMultsForAString(s.substr(startIndex, length));

                startIndex = endIndex;
                go = true;
            }

            // 4. We only see the don't() match.
            else
            {
                endIndex = startIndex + dontMatch.position(0) + dontString.size();
                int length = endIndex - startIndex + 1;

                if (go)
                    retval += calculateMultsForAString(s.substr(startIndex, length));

                startIndex = endIndex;
                go = false;
            }
        }
    }

    return retval;
}

int main(void)
{
    std::vector<string> input = FileHelpers::ReadFileIntoStrings(FILENAME);

    PART1(part1(input));
    PART2(part2(input));

    return 0;
}