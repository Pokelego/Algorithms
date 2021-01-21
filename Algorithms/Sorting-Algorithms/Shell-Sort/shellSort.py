"""
Selection sort is an algorithm which can be thought of as a more efficient insertion sort because
elements a distance apart are being compared rather than adjacent

Time Complexity is O(n log^2 n)

"""

def shellSort(array):
   # The distance between each value being compared
   gap = len(array) // 2

   while gap != 0:
      current = gap

      while current < (len(array)):
         temp = array[current]
         i = current - gap

         while i >= 0 and temp < array[i]:
            array[i + gap] = array[i]
            i -= gap

         array[i + gap] = temp
         current += 1

      gap //= 2