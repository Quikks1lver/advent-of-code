#pragma once

#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::string;

class FileHelpers
{
public:
    // To signify a NaN in 2D int array readings.
    static const int INVALID_2D_ARR_SPOT;
    
    // Reads a given file line by line into strings.
    static std::vector<string> ReadFileIntoStrings(const string& filepath);

    // Specially for ints, reads file into 2D array.
    // If a NaN is seen, a INVALID_2D_ARR_SPOT is placed in that location.
    static std::vector<std::vector<int>> Read2DIntArray(const string& filepath);

    // Reads a given file line by line into vectors of whatever.
    template <typename T>
    static std::vector<std::vector<T>> ReadFileIntoListOfLists(const string& filepath)
    {
        std::vector<std::vector<T>> outputLines;

        std::ifstream inputFile(filepath);

        if (!inputFile.is_open())
        {
            throw std::ios_base::failure("Failed to open " + filepath);
        }

        string line;
        while (std::getline(inputFile, line))
        {
            std::istringstream lineStream(line);
            std::vector<T> row;
            T type;

            while (lineStream >> type)
            {
                row.push_back(type);
            }

            outputLines.push_back(std::move(row));
        }

        return outputLines;
    }
};

/*
Why do we have a template declaration here?
From AI...

The Problem:

The instantiation of a template happens when the compiler sees its usage in a translation unit (source file).
If the implementation of the template is in a separate .cpp file:

    The compiler compiling the .cpp file using the template has no access to the implementation.
    This results in linker errors like "undefined symbols".

Why Header Files Fix It:

By placing the entire template definition (declaration and implementation) in a header file:

    Every translation unit that includes the header has access to the full template definition.
    The compiler can generate and instantiate the specific template code it needs for the given type.

Comparison with Regular Functions:

    Regular Functions: Only need the declaration (in a header) to compile because their definitions
    are fully compiled and linked separately.
    Templates: Need both declaration and implementation available during compilation because they
    aren't fully compiled until instantiated.
*/