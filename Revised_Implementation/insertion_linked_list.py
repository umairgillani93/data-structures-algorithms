# Start off with the imports 
from travers2 import Node
from travers2 import SinglyLinkedList

# Declare linked-list nodes
head_node = SinglyLinkedList()
head_node.head_val = Node("Head Node")
second_node = Node("Second Node")
third_node = Node("Third Node")

# Declare pointers
head_node.head_val.next_node = second_node
head_node.head_val.next_node.next_node = third_node

def _insert():
  new_node = Node('New Node')
  head_node.head_val = new_node
  new_node.next_node = head_node.head_val


head_node = SinglyLinkedList()
head_node.head_val = Node("Head Node")
second_node = Node("Second Node")
third_node = Node("Third Node")

# Declare pointers
head_node.head_val.next_node = second_node
head_node.head_val.next_node.next_node = third_node

new_node = Node('New Node')
head_node.head_val = new_node
new_node.next_node = head_node.head_val

print('head_node: {}'.format(head_node.head_val.data))
