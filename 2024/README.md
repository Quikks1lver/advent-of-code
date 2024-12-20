I wanted to get better with C++ this year. It's definitely more challenging to use for these puzzles than something like Python, but great learnings!

# C++ Build Process

This project uses a `Makefile` to automate the process of compiling and linking C++ source files for each day's challenge (e.g., `day01.cpp`, `day02.cpp`, etc.). Below is a simple explanation of how the build process works.

## Folder Structure

- **`Helpers/`**: Contains helper functions, like `FileHelpers.h` and `FileHelpers.cpp`, that are used by the `dayXX.cpp` files.
- **`day01.cpp`, `day02.cpp`, ..., `day25.cpp`**: Each file contains the C++ source code for a specific day's challenge.
- **`Makefile`**: The file used to automate the build process.

## How the Build Process Works

### 1. **Makefile Overview**

The `Makefile` defines how the project is built. It includes:

- **Compiler settings**: Specifies which compiler to use (e.g., `g++`) and flags for compiling (`-std=c++17 -Wall`).
- **Object files**: Defines rules for compiling `.cpp` files into `.o` object files.
- **Linking**: Combines object files into final executables (e.g., `day01`, `day02`).

### 2. **How to Use the Makefile**

#### 1. **Build All Executables**

To compile all the `dayXX.cpp` files into their respective executables (`day01`, `day02`, ..., `day25`), run:

```bash
# From project root
cd 2024/
make
```

#### 2. **Build Specific Executable**

To compile a particular day, ex `day01.cpp`, simply run:

```bash
make day01
```

#### 3. **Run Specific Executable**

Running Step (2) will give you an executable. Simply run like so:

```bash
./day01
```

Sample output (yes, the code has macros to time each part!):

```txt
Part 1 : 123 (0.004542 ms)
Part 2 : 456 (0.294792 ms)
```

_Note: this README and build process was helped along with OpenAI._
