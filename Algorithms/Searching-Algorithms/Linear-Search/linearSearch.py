"""An algorithm which goes through every item in a list until it finds a given item and returns its index"""

def linearSearch(array, item):
   for i, val in enumerate(array):
      if val == item:
         return i