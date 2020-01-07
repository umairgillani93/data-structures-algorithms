# Creating the Node class for Single Linked-List
class Node(object):
    """A Singly Linked-List has ordered lists in each Node, which carries the Address of 
    current stored item and Address of the next Node."""

    def __init__(self, value):
        self.value = value 
        self.nextnode = None 

    
a = Node(1)
b = Node(2)
c = Node(3)

# creating the next nodes 
a.nextnode = b 
b.nextnode = c 


print(a.value)
print(b.value)
print(c.value)

print(a.nextnode.value)
print(b.nextnode.value)