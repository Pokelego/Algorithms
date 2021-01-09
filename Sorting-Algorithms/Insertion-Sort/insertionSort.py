"""
Insertion sort is an algorithm which goes through a list one by on and compares it to every other item and shifts it accordingly

Time Complexity is O(n^2)

"""

def insertionSort(array):
   for i in range(1, len(array)):
      current = array[i]
      j = i - 1
      while j >= 0 and array[j] > current:
         array[j+1] = array[j]
         j -= 1
      array[j+1] = current
