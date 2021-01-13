import sys

class MinHeap:
   def __init__(self, max_size):
      self.max_size = max_size
      self.size = 0
      self.heap = [0]*(self.max_size + 1)
      self.heap[0] = -1 * sys.maxsize
      self.front = 1

   def insert(self, data):
      # Inserts a node into the heap
      if self.size >= self.max_size:
         return

      self.size += 1
      self.heap[self.size] = data

      current = self.size

      while self.heap[current] < self.heap[self.parent(current)]:
         self.swap(current, self.parent(current))
         current = self.parent(current)
      
      self.minHeap()

   def delete(self):
      # Deletes the smallest node from the heap and returns it
      deleted = self.heap[self.front]
      self.heap[self.front] = self.heap[self.size]
      self.size -= 1
      self.minHeapify(self.front)
      return deleted

   def parent(self, position):
      # Returns position of parent node
      return position//2

   def leftChild(self, position):
      # Returns position of left child of current node
      return 2 * position

   def rightChild(self, position):
      # Returns position of right child of current node
      return (2 * position) + 1

   def isLeaf(self, position):
      # Returns true if the node is a leaf
      if position >= (self.size//2) and position <= self.size:
         return True
      return False

   def swap(self, position1, position2):
      # Swaps two nodes in the heap
      self.heap[position1], self.heap[position2] = self.heap[position2], self.heap[position1]

   def minHeapify(self, position):
      # Maintains the heap structure of a specific node
      if not self.isLeaf(position):
         if self.heap[position] > self.heap[self.leftChild(position)] or self.heap[position] > self.heap[self.rightChild(position)]:
            # Swap left child
            if self.heap[self.leftChild(position)] < self.heap[self.rightChild(position)]:
               self.swap(position, self.leftChild(position))
               self.minHeapify(self.leftChild(position))
            # Swap right child
            else:
               self.swap(position, self.rightChild(position))
               self.minHeapify(self.rightChild(position))


   def minHeap(self):
      # Maintains the heap structure of the entire heap
      for position in range(self.size//2, 0, -1):
         self.minHeapify(position)