# Handy data structures

from typing import Any, List, Union

# This is a bit cheeky, as Lists can act like stacks, but it's useful for the problem anyhow xD
class Stack:
   """
   A LIFO data structure, holding any values
   """
   def __init__(self):
      self._stack: List[Any] = []
   
   def push(self, data: Any) -> None:
      """
      Pushes a value onto the stack
      """
      self._stack.append(data)
   
   def pop(self) -> Union[Any, None]:
      """
      Pops and returns val from top of stack. If empty, returns none
      """
      if len(self._stack) > 0:
         return self._stack.pop()
      return None
   
   def peek(self) -> Any:
      """
      Returns val at top of stack. If empty, returns none
      """
      if len(self._stack) > 0:
         return self._stack[-1]
      return None
   
   def getSize(self) -> int:
      """
      Returns current size of stack
      """
      return len(self._stack)

   def clearOut(self) -> None:
      """
      Clears stack
      """
      self._stack.clear()

   def __repr__(self):
      return str(self._stack)