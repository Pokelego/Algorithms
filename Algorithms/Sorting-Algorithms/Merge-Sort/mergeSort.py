"""
Merge sort is an algorithm which repeatedly splits an arrays into two sub arrays until each one is only a length of two 
and then sorts each arrays and merges two together, 
this is repeated until array is fully merged and sorted

Time Complexity is O(n log(n))

"""


def mergeSort(array):
   if len(array) > 1:
      # Split array into left and right sub-arrays
      middle = len(array)//2
      left = array[:middle]
      right = array[middle:]

      mergeSort(left)
      mergeSort(right)

      left_index = right_index = index = 0

      # Sorting logic
      while left_index < len(left) and right_index < len(right):
         if left[left_index] < right[right_index]:
            array[index] = left[left_index]
            left_index += 1
         else:
            array[index] = right[right_index]
            right_index += 1
         index += 1

      # Make sure every element is included
      while left_index < len(left):
         array[index] = left[left_index]
         left_index += 1
         index += 1

      while right_index < len(right):
         array[index] = right[right_index]
         right_index += 1
         index += 1

