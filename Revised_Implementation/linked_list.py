# Singly Linked-List implementation by Umairgillani -> Umairgillani93@gmail.com

class Node:
  '''
  Node class. Will us this to create 
  nodes in singly linked-list
  '''
  def __init__(self, data):
    self.data = data
    self.next = None

class SinglyLinkedList:
  '''
  Actual singly linked-list class
  '''
  def __init__(self):
    self.head_val = None

  def _traverse(self):
    '''
    traverse the linked-list
    '''
    # declare first node value
    show_val = self.head_val
    
    # While next node pointer is not None:
    # Note: only last node has next pointer equals None
    while show_val is not None:
      print('\nnode value is : {}'.format(show_val.data))
      show_val = show_val.next


node1 = SinglyLinkedList()
node1.head_val = Node("First Node")
node2 = Node("Second Node")
node3 = Node("Third Node")

# Set the pointers nw
node1.head_val.next = node2
node1.head_val.next.next = node3

# Print the data objects and pointers
print('Node1 data: {}'.format(node1.head_val.data))
print('Node2 data: {}'.format(node2.data))
print('Node2 address: {}'.format(node2.next))
print('Node3 data: {}'.format(node3.data))
print('Node3 address: {}'.format(node3.next))

# Call _traverse() function
node1._traverse()
