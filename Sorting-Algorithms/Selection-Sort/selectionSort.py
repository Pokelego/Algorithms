"""
Selection sort is an algorithm which repeatedly selects the next-smallest element and swap it into place

Time Complexity is O(n^2)

"""

def selectionSort(array):
   for i in range(len(array)):
      min_index = i
      for j in range(i+1, len(array)):
         if array[j] < array[min_index]:
            min_index = j

      array[i], array[min_index] = array[min_index], array[i]
