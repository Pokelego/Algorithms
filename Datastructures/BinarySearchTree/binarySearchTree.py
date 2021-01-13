class Node:
   def __init__(self, data):
      self.data = data
      self.right = None
      self.left = None

class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insert(self, data):
      if self.root is None:
         self.root = Node(data)
      else:
         self._insertNode(self.root, data)

   def _insertNode(self, current_node, data):
      if data <= current_node.data:
         if current_node.left:
            self._insertNode(current_node.left, data)
         else:
            current_node.left = Node(data)
      else:
         if current_node.right:
            self._insertNode(current_node.right, data)
         else:
            current_node.right = Node(data)

   def delete(self, data):
      if self.root is None:
         return
      else:
         self.root = self._deleteNode(self.root, data)

   def _deleteNode(self, current_node, data):
      # Recursion until data is found
      if data < current_node.data:
         current_node.left = self._deleteNode(current_node.left, data)
      elif data > current_node.data:
         current_node.right = self._deleteNode(current_node.right, data)
      
      else:
         if current_node.left is None:
            temp = current_node.right
            current_node = None
            return temp
         elif current_node.right is None:
            temp = current_node.left
            current_node = None
            return temp

         temp = findMin(current_node.right)
         current_node.data = temp.data
         current_node.right = self._deleteNode(current_node.right, temp.data)

      return current_node 


# Utility Functions
def preorder(root):
   if root:
      print(root.data, end=" ")
      preorder(root.left)
      preorder(root.right)

def postorder(root):
   if root:
      postorder(root.left)
      postorder(root.right)
      print(root.data, end=" ")

def inorder(root):
   if root:
      inorder(root.left)
      print(root.data, end=" ")
      inorder(root.right)

def findMin(root):
   if root is None:
      return

   if root.left is None:
      print(root.data)
      return root
   findMin(root.left)

def findMax(root):
   if root is None:
      return

   if root.right is None:
      print(root.data)
      return root
   findMax(root.right) 

def findParent(root, data):
   if data == root.data or root is None:
      return

   if data < root.data:
      if root.left is None:
         return
      elif root.left.data == data:
         return root
      else:
         findParent(root.left, data)

   else:
      if root.right is None:
         return
      elif root.right.data == data:
         return root
      else:
         findParent(root.right, data)   

def findNode(root, data):
   if root is None:
      return

   if root.data == data:
      return root
   elif data < root.data:
      return findNode(root.left, data)
   else:
      return findNode(root.right, data)

def containsNode(root, data):
   if root is None:
      return False

   if root.data == data:
      return True
   elif data < root.data:
      return containsNode(root.left, data)
   else:
      return containsNode(root.right, data)

def numberOfChildren(node):
   num_children = 0
   if node.left:
      num_children += 1
   if node.right:
      num_children += 1
   return num_children
