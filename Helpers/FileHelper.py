# File readers for use elsewhere

def readFile(filename: str) -> list:
   """
   Reads a file and returns a list of the data
   """
   
   try:
      with open(filename, "r") as fp:
         return fp.readlines()
   except:
      raise Exception(f"Failed to open {filename}")