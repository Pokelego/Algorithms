"""
Binary search is an effective algorithm for finding an item in a sorted list
This is done by repeadedly dividing the list in half until the item is found 
Runs in logarthmic time O(log n) where n is the size of the array

"""

def binary_search(alist, target):
   guess = 0
   min_num = 0
   max_num = len(alist)-1
   while max_num >= min_num:
      guess = (min_num + max_num) // 2
      if alist[guess] == target:
         print(str(alist[guess]) + " found at index: " + str(guess))
         return guess
      elif alist[guess] < target:
         min_num = guess + 1
      else:
         max_num = guess - 1
   return -1

