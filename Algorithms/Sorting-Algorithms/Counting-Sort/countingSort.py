"""
Counting sort is an algorithm which finds the max element in an array and creates a new array of size length+1
Store each elements respective count, then stores a cumulative count of the two arrays into an output array

Time Complexity is O(n + k)

"""

def countingSort(array):
   # k is the highest possible number to count to
   k = max(array) + 1

   size = len(array)
   out = [0] * size

   count = [0] * k

   for i in range(0, size):
      count[array[i]] += 1

   for i in range(1, k):
      count[i] += count[i-1]

   i = size -1
   while i >= 0:
      out[count[array[i]]-1] = array[i]
      count[array[i]] -= 1
      i -= 1
   for i in range(0, size):
      array[i] = out[i]
