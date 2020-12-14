# Binary functions

def convertBinaryToDecimal(num: str) -> int:
   """
   Converts a binary string to a decimal number
   """
   multiplier: int = 1
   decimalNum: int = 0

   for c in reversed(num):
      decimalNum += (int(c) * multiplier)
      multiplier *= 2
   
   return decimalNum