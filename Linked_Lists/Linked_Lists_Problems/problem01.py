# Problem01: Linked List Reversal
"""Write a function to reverse a Linked List in place. The function will take
in the head of the list as input, and return the new head of the list """

# Lets first create a linked list
class SinglyNode(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

node0 = SinglyNode(0)
node1 = SinglyNode(1)
node2 = SinglyNode(2)

node0.nextnode = node1
node1.nextnode = node2

print(node0.value)
print(node1.value)
print(node2.value)

print(node0.nextnode.value)
print(node1.nextnode.value)

def reverse_linkedlist(head):
    """we wanna do create this function in O(1) space.
    which means we don't want to create a new list or clone array
    so we will simple use the current Nodes. Also time-wise we can
    perform the reversal in O(n) time """

    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode
        current.nextnode = previous
        previous = current
        current = nextnode

    return previous

reverse = reverse_linkedlist(node0)
print(reverse)

# print(node0.nextnode.value)
print(node2.nextnode.value)
print(node1.nextnode.value)
