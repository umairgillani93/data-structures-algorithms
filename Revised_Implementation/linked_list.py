# Singly Linked-List implementation by Umairgillani -> Umairgillani93@gmail.com

class Node:
  '''
  Node class. Will us this to create 
  nodes in singly linked-list
  '''
  def __init__(self, data):
    self.data = data
    self.next_node = None

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
      show_val = show_val.next_node


  def _insert(self, data):
    '''
    inserts new node at head position of
    singly linked-list
    '''
    print('\nInserting at head\'s position')
    # Initialize a new node
    new_node = Node(data)

    # Declare next_node of this new node as head node
    new_node.next_node = self.head_val
    
    # Pass the data the of new_node to head
    self.head_val = new_node




node1 = SinglyLinkedList()
node1.head_val = Node("First Node")
node2 = Node("Second Node")
node3 = Node("Third Node")

# Set the pointers nw
node1.head_val.next_node  = node2
node1.head_val.next_node.next_node  = node3

# Print the data objects and pointers
print('Node1 data: {}'.format(node1.head_val.data))
print('Node2 data: {}'.format(node2.data))
print('Node2 address: {}'.format(node2.next_node))
print('Node3 data: {}'.format(node3.data))
print('Node3 address: {}'.format(node3.next_node))

# Call _traverse() function
#node1._traverse()
#node1._insert('new_node')

print("\n")
print(node1._traverse())
