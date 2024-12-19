from enum import Enum
from Helpers.FileHelpers import read_lines
from typing import List, Tuple, Union
FILEPATH = "2022/Input/day07.txt"

class Operation():
    class Type(Enum):
        CD = 0
        LS = 1
        DIR = 2
        FILE = 3
    
    def __init__(self, line: str) -> None:
        self.type: Operation.Type = None
        self.payload: Union[str, Tuple[int, str]] = None

        components = line.split()
        if components[0] == '$':
            if components[1] == 'cd':
                self.type = Operation.Type.CD
                self.payload = components[2]
            else:
                self.type = Operation.Type.LS
        elif components[0] == 'dir':
            self.type = Operation.Type.DIR
            self.payload = components[1]
        else:
            self.type = Operation.Type.FILE
            self.payload = (int(components[0]), components[1])

class File():
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

class Directory(File):
    LARGE_DIRECTORIES_THRESHOLD = 100000
    TOTAL_DISK_SPACE = 70000000
    UPDATE_SPACE = 30000000

    def __init__(self, name: str, size: int, parent) -> None:
        super().__init__(name, size)
        self.parent: Directory = parent
        self.children: List[Union[Directory, File]] = list()
    
    def add_child(self, item):
        self.children.append(item)
    
    def get_directory(self, directory: str):
        for child in self.children:
            if child.name == directory and type(child) == Directory:
                return child

    def sum_large_directories(self) -> int:
        class GlobalSum():
            def __init__(self): self.sum = 0
            def add(self, num: int): self.sum += num
        
        def recurse(directory: Directory, summation: GlobalSum):
            for child in directory.children:
                if type(child) == File:
                    directory.size += child.size
                else:
                    recurse(child, summation)
                    directory.size += child.size

            if directory.size < Directory.LARGE_DIRECTORIES_THRESHOLD:
                summation.add(directory.size)
        
        summation = GlobalSum()
        recurse(self, summation)
        return summation.sum

    def find_smallest_directory_to_free(self) -> int:
        class GlobalList():
            def __init__(self): self.listy = []
            def add(self, num: int): self.listy.append(num)
        
        def recurse(directory: Directory, space_list: GlobalList):
            for child in directory.children:
                if type(child) == Directory:
                    recurse(child, space_list)
                    space_list.add(child.size)
        
        space_list = GlobalList()
        space_list.add(self.size)
        recurse(self, space_list)

        needed_space = Directory.UPDATE_SPACE - (Directory.TOTAL_DISK_SPACE - self.size)
        
        space_list.listy.sort()
        for value in space_list.listy:
            if value >= needed_space:
                return value
    
    @staticmethod
    def build_file_system(input: List[str]):
        root_directory = Directory("/", 0, None)
        current_directory = root_directory

        i = 0
        while i < len(input):
            op = Operation(input[i])

            if op.type == Operation.Type.CD:
                if op.payload == '..':
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.get_directory(op.payload)
                i += 1
            else:
                i += 1
                while i < len(input):
                    op = Operation(input[i])
                    if op.type == Operation.Type.CD:
                        break
                    if op.type == Operation.Type.DIR:
                        current_directory.add_child(Directory(op.payload, 0, current_directory))
                    else:
                        current_directory.add_child(File(op.payload[1], op.payload[0]))
                    i += 1

        return root_directory

def main():
   root_directory = Directory.build_file_system([line.strip() for line in read_lines(FILEPATH)][1:])
   print(f"Part 1 -- {root_directory.sum_large_directories()}")
   print(f"Part 2 -- {root_directory.find_smallest_directory_to_free()}")

if __name__ == "__main__": main()