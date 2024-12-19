# Compiler to use
CXX = g++
CXXFLAGS = -std=c++11 -Wall  # Use C++17 standard and enable all warnings
LDFLAGS =  # Linker flags (none for this example)

# Directories
SRC_DIR = .
INCLUDE_DIR = Helpers

# Common source files
COMMON_SRCS = $(INCLUDE_DIR)/FileHelpers.cpp

# Object files for common code (FileHelpers)
COMMON_OBJS = $(COMMON_SRCS:.cpp=.o)

# Rule to compile each dayXX.cpp separately
DAY_SRCS = $(wildcard $(SRC_DIR)/day[0-9][0-9].cpp)

# Object files for each dayXX.cpp
DAY_OBJS = $(DAY_SRCS:.cpp=.o)

# Output executable names (day01, day02, ..., day25)
TARGETS = $(DAY_SRCS:$(SRC_DIR)/%.cpp=$(SRC_DIR)/%)

# Default target
all: $(TARGETS)

# Rule for compiling object files from dayXX.cpp files
$(SRC_DIR)/%.o: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

# Rule for linking the object files into the final executables
$(SRC_DIR)/day%: $(SRC_DIR)/day%.o $(COMMON_OBJS)
	$(CXX) $^ -o $@ $(LDFLAGS)

# Clean up compiled files
clean:
	rm -f $(COMMON_OBJS) $(DAY_OBJS) $(TARGETS)

# Phony targets (not actual files)
.PHONY: all clean
