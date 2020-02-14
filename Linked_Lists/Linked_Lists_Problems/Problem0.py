# Problem0: Singly Linked List Cycle Check
"""Given a single linked list, write a funciton which takes in the first
node in singly linked list and returns Boolean indicating if the linked
list contains a cycle"""

# Lets first implement our Single lined list
class SinglyNode(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

first_node = SinglyNode(1)
second_node = SinglyNode(2)
third_node = SinglyNode(3)

first_node.nextnode = second_node
second_node.nextnode = third_node

first_node.prevnode = third_node

print(first_node.value, second_node.value, third_node.value)
print(first_node.nextnode.value)
print(second_node.nextnode.value)

def cycle_check(node):
    # nodes = [first_node, second_node, third_node]

    # for node in nodes:
    if node.prevnode is None:
        return False
    else:
        return True

is_cyclic = cycle_check(first_node)
print(is_cyclic)
