import time
from typing import Callable

def __timeFunction(prefix: str, func: Callable, *args) -> None:
    """
    Times the execution of a function and prints result.
    """

    start_time = time.time()
    retval = func(*args)
    end_time = time.time()
    
    full_time_ms = (end_time - start_time) * 1000
    
    print(f"{prefix} : {retval} ({full_time_ms:.3f} ms)")

def PART1(func: Callable, *args) -> None:
    __timeFunction("Part 1", func, *args)

def PART2(func: Callable, *args) -> None:
    __timeFunction("Part 2", func, *args)