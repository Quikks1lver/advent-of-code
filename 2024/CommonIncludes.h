#pragma once

#include <chrono>
#include <cmath>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <regex>
#include <sstream>

using std::string;
using std::cout;
using std::endl;

#define _PARTX_WITH_TIMING(x, str) { \
    auto start = std::chrono::high_resolution_clock::now(); \
    auto result = (x); \
    auto end = std::chrono::high_resolution_clock::now(); \
    std::chrono::duration<double, std::milli> duration = end - start; \
    cout << "Part " << str << " : " << result << " (" << duration.count() << " ms)" << endl; \
}

// Macro to print out part 1 answer.
#define PART1(x) _PARTX_WITH_TIMING(x, 1)

// Macro to print out part 2 answer.
#define PART2(x) _PARTX_WITH_TIMING(x, 2)

// Referenced from AI as help.
// We need this to throw std::pairs into a hash set (unordered_set).
namespace std
{
    template <>
    struct hash<std::pair<int, int>>
    {
        size_t operator()(const std::pair<int, int>& p) const
        {
            // Use a combination of the two integers to create a unique hash value.
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };
}

namespace Helpers
{
    // Prints a 2D array.
    template <typename T>
    void printDoubleArray(const std::vector<std::vector<T>>& arr)
    {
        for (const auto& row : arr)
        {
            for (const auto& element : row)
                cout << element << " ";
            cout << endl;
        }
    }

    // Determines whether a (row, col) is in bounds for a 2D array.
    template <typename T>
    bool isInbounds(const std::vector<std::vector<T>>& arr, int row, int col)
    {
        return row >= 0 && col >= 0 && row < arr.size() && col < arr[row].size();
    }
}
