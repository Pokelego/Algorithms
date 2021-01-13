class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class SinglyLinkedList:
   def __init__(self):
      self.head = None

   def append(self, data):
      node = Node(data)

      # Add node at front if list is empty
      if self.head is None:
         self.head = node
         return

      # Add node at the end of the list
      last = self.head
      while last.next:
         last = last.next
      last.next = node

   def prepend(self, data):
      node = Node(new_data)
      node.next = self.head
      self.head = node

   def delete(self, value):
      temp = self.head

      # Check is value is not present
      if temp == None:
         return

      # Delete head 
      if temp is not None:
         if temp.data = value:
            self.head = temp.next
            temp = None
            return
      
      # Delete at location
      while temp is not None:
         if temp.data == value:
            break
      prev = temp
      temp = temp.next

      prev.next = temp.next
      temp = None

   def display(self):
      temp = self.head
      while temp is not None:
         print(temp)
         temp = temp.next
