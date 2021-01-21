class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
      self.prev = None

class DoublyLinkedList:
   def __init__(self):
      self.head = None

   def prepend(self, data):
      node = Node(data)
      node.next = self.head
      node.prev = None

      if self.head is not None:
         self.head.prev = node
      
      self.head = node

   def append(self, data):
      node = Node(data)
      last = self.head
      node.next = None

      # Node becomes head if list is empty
      if self.head is None:
         node.prev = None
         self.head = node
         return
      
      while last.next is not None:
         last = last.next

      last.next = node
      node.prev = last
   
   def display(self):
      last = None
      node = self.head
      # Beginning to end
      while node is not None:
         print(node.data)
         last = node
         node = node.next

      # End to beginning
      while last is not None:
         print(last.data)
         last = last.prev