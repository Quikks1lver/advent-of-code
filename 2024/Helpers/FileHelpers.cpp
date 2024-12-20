#include "FileHelpers.h"

#include <iostream>
#include <stdexcept>

const int FileHelpers::INVALID_2D_ARR_SPOT = -1;

std::vector<string> FileHelpers::ReadFileIntoStrings(const string& filepath)
{
    std::vector<string> outputLines;

    // RAII means when this var goes out of scope, file handle is cleaned up.
    std::ifstream inputFile(filepath);

    if (!inputFile.is_open())
    {
        throw std::ios_base::failure("Failed to open " + filepath);
    }

    string line;
    while (std::getline(inputFile, line))
    {
        outputLines.push_back(std::move(line));
    }

    return outputLines;
}

std::vector<std::vector<int>> FileHelpers::Read2DIntArray(const std::string& filepath)
{
    std::vector<std::vector<int>> outputLines;
    std::ifstream inputFile(filepath);

    if (!inputFile.is_open())
    {
        throw std::ios_base::failure("Failed to open " + filepath);
    }

    string line;
    while (std::getline(inputFile, line))
    {
        std::vector<int> row;

        for (char ch : line)
            row.push_back(std::isdigit(ch)
                          ? ch - '0'
                          : FileHelpers::INVALID_2D_ARR_SPOT);
        
        outputLines.push_back(std::move(row));
    }

    return outputLines;
}
