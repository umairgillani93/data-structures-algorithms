class Node:
  def __init__(self, data):
    self.data= data 
    self.next_node = None


class SinglyLinkedList:
  def __init__(self):
    self.head_val = None

  def _traverse(self):
    head_node = self.head_val
    while head_node is not None:
      print('\nNode Value: {}'.format(head_node.data))
      head_node = head_node.next_node


