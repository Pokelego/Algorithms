"""
Bubble sort is an algorithm which steps through the array and if an elements is out of order, swap elements

Time Complexity is O(n^2)

"""

def bubbleSort(array):
   is_sorted = False
   last_unsorted = len(array)-1

   while not is_sorted:
      is_sorted = True
      for i in range(last_unsorted):
         if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            is_sorted = False
      last_unsorted -= 1
