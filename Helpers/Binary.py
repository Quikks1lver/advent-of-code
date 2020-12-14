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

def convertDecimalToBitString(num: str) -> str:
   """
   Converts a decimal string to a bit string
   """
   num = int(num)
   bitString: str = ""

   while num > 0:
      remainder = num % 2
      num = num // 2
      bitString = str(remainder) + bitString
   
   return bitString