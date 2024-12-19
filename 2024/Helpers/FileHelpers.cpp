#include "FileHelpers.h"

#include <iostream>
#include <stdexcept>

std::vector<string> FileHelpers::ReadFileIntoStrings(string filepath)
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
