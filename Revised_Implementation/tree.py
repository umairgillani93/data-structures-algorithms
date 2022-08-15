# Binary Tree implementation in Python by Umair Gillani -> Umairgillani93@gmail.com

class TreeNode:
  '''
  Node of a binary Tree
  '''
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None 

  def print_tree(self):
    '''
    prints the data of tree
    '''
    if self.left:
      self.left.print_tree()
    
    print(self.data)
    if self.right:
      self.right.print_tree()

  def _insert(self, data):
    '''
    inserts data in Binary tree. Since it's a balanced binary-tree,
    so we'll have to check the value of data, compare it with root
    and then insert on left or right side accordingly
    '''
    # check if binary-tree has root
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = TreeNode(data)
        
        else:
          self.left._insert(data)

      elif data > self.data:
        if self.right is None:
          self.right = TreeNode(data)

        else:
          self.right._insert(data)


    else:
      self.data = data
    

# Instantiate the TreeNode
root = TreeNode(10)
root._insert(6)
root._insert(14)
root._insert(5)
root._insert(3)
root.print_tree()
