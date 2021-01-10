"""
Quick sort is an algorithm which creates a pivot point and swap elements 
such that elements less than the pivot are before and ones greater than come after, 
repeat on halves until sorted

Time Complexity is O(n log(n))

"""

def quickSort(array):
   _quickSort(array, 0, len(array)-1)

def _quickSort(array, left, right):
   # Recursive function
   if left >= right:
      return
   pivot = array[(left + right)//2] # Pivot element is the center

   index = partition(array, left, right, pivot)

   _quickSort(array, left, index-1) # Left side
   _quickSort(array, index, right) # Right side

def partition(array, left, right, pivot):
   while left <= right:
      while array[left] < pivot:
         # Move left index towards pivot
         left += 1
      while array[right] > pivot:
         # Move right index towards pivot
         right -= 1

      if left <= right:
         array[left], array[right] = array[right], array[left] # Swaps elements
         left += 1
         right -= 1

   return left # The dividing index between the left and right side

