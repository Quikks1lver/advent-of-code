import time
from typing import Any, Callable

# Syntax of [..., Any] -> function accepts any arguments, and returns Any.
def __timeFunction(prefix: str, func: Callable[..., Any], *args: Any) -> None:
    """
    Times the execution of a function and prints result.
    """

    start_time = time.time()
    retval = func(*args)
    end_time = time.time()
    
    full_time_ms = (end_time - start_time) * 1000
    
    print(f"{prefix} : {retval} ({full_time_ms:.3f} ms)")

def PART1(func: Callable[..., Any], *args: Any) -> None:
    __timeFunction("Part 1", func, *args)

def PART2(func: Callable[..., Any], *args: Any) -> None:
    __timeFunction("Part 2", func, *args)