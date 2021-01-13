class Node():
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
      self.height = 1

class AVLTree():
   def insert(self, root, data):
      # Normal Binary Search Tree insertion
      if root is None:
         return Node(data)
      elif data < root.data:
         root.left = self.insert(root.left, data)
      else:
         root.right = self.insert(root.right, data)

      # Update height of tree through checking the highest height on both left and right subtrees and then adding one to it
      root.height = self.updateHeight(root)

      # Get balance factor (left height - right height) for the following balance statements
      # If balance is ever more than or less than one, the tree needs to be balanced
      balance = self.getBalance(root)

      # Balancing logic
      # Very Left skewed tree
      if balance > 1 and data < root.left.data: 
         return self.rightRotate(root)

      # Very Right skewed tree
      if balance < -1 and data > root.right.data: 
         return self.leftRotate(root)

      # Slightly Left skewed tree
      if balance > 1 and data > root.right.data: 
         root.left = self.leftRotate(root.left)
         return self.rightRotate(root)

      # Slightly Right skewed tree
      if balance < -1 and data < root.right.data: 
         root.right = self.rightRotate(root.right)
         return self.leftRotate(root)

      return root

   def delete(self, root, data):
      # Normal Binary Search Tree deletion
      if root is None:
         return root
      elif data < root.data:
         root.left = self.delete(root.left, data)
      elif data > root.data:
         root.right = self.delete(root.right, data)
      else:
         if root.left is None:
            temp = root.right
            root = None
            return temp
         elif root.right is None:
            temp = root.left
            root = None
            return temp

         temp = self.findMin(root.right)
         root.data = temp.data
         root.right = self.delete(root.right, temp.data)
      
      # Update height of tree through checking the highest height on both left and right subtrees and then adding one to it
      root.height = self.updateHeight(root)

      # Get balance for the following balance statements
      # If balance is ever more than or less than one, the tree needs to be balanced
      balance = self.getBalance(root)

      # Balancing logic
      # Very left skewed tree (Left-Left)
      if balance > 1 and self.getBalance(root.left) >= 0:
         return self.rightRotate(root)

      # Very right skewed tree (Right-Right)
      if balance < -1 and self.getBalance(root.right) <= 0:
         return self.leftRotate(root)
      
      # Slightly left skewed tree (Left-Right)
      if balance > 1 and self.getBalance(root.left) < 0:
         root.left = self.leftRotate(root.left)
         return self.rightRotate(root)

      # Slightly right skewed tree (Right-Left)
      if balance < -1 and self.getBalance(root.right) > 0:
         root.right = self.rightRotate(root.right)
         return self.leftRotate(root)

      return root

   # -----Helper Functions----- #
   def rightRotate(self, current_node):
      # Node goes to the right in order to balance
      new_node = current_node.left
      temp = new_node.right

      # Rotate
      new_node.right = current_node
      current_node.left = temp

      # Update height of nodes
      current_node.height = self.updateHeight(current_node)
      new_node.height = self.updateHeight(new_node)

      return new_node

   def leftRotate(self, current_node):
      # Node goes to the left in order to balance
      new_node = current_node.right
      temp = new_node.left

      # Rotate
      new_node.left = current_node
      current_node.right = temp

      # Update height of nodes
      current_node.height = self.updateHeight(current_node)
      new_node.height = self.updateHeight(new_node)

      return new_node

   def getBalance(self, root):
      # Returns the height difference between left and right subtrees
      if root is None:
         return 0
      return self.getHeight(root.left) - self.getHeight(root.right)

   def getHeight(self, node):
      # Returns the height of the node
      if node is None:
         return 0
      return node.height

   def updateHeight(self, node):
      # Updates the height of the current node
      return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

   def findMin(self, root):
      # Goes down the left subtree until bottom left node is found and returns it
      if root is None or root.left is None:
         return root
      return self.getMinValueNode(root.left)

   # -----Utility Functions----- #
   def preOrder(self, root):
      if root:
         print(root.data, end=" ")
         self.preOrder(root.left)
         self.preOrder(root.right)

   def postOrder(self, root):
      if root:
         self.postOrder(root.left)
         self.postOrder(root.right)
         print(root.data, end=" ")

   def inOrder(self, root):
      if root:
         self.inOrder(root.left)
         print(root.data, end=" ")
         self.inOrder(root.right)