"""
Counting sort is an algorithm which sorts elements by counting the number of occurences of each unique item
then sorts each item by mapping the count as an index into a new array

Time Complexity is O(n + k)

"""

def countingSort(array):
   # k is the highest possible number to count to
   k = max(array) + 1

   size = len(array)
   out = [0] * size

   count = [0] * k

   for i in range(0, size):
      # stores the count of each unique value
      count[array[i]] += 1

   for i in range(1, k):
      # stores the total count
      count[i] += count[i-1]

   i = size -1
   while i >= 0:
      # place elements into output array and decrease the count of every unique item
      out[count[array[i]]-1] = array[i]
      count[array[i]] -= 1
      i -= 1
   for i in range(0, size):
      array[i] = out[i]
