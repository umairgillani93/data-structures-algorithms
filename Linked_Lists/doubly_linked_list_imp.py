# Implementing Doubly Linked-List 
class Node(object):
    """A Doubly Linked-List is a linked-list, which has address for the previous Node 
    as well as the next Node, along with the value of current Item"""

    def __init__(self, value):
        self.value = value 
        self.next_node = None 
        self.prev_node = None 

a = Node(0)
b = Node(1)
c = Node(2) 

a.next_node = b 
b.next_node = c 

c.prev_node = b 
b.prev_node = a 

print(a)
print(b)
print(c)

print(a.next_node.value)
print(b.next_node.value)

print(c.prev_node.value)
print(b.prev_node.value)