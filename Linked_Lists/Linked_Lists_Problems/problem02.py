# Problem02: Linked List Nth to Last Node
"""
Write a function that takes a Head node and an Integer value "n", and
then returns the "nth" to last Node in the linked list.
"""
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

def nth_to_last_node(n, head):
    left_pointer = head # head pointer
    right_pointer = head # pointer which is "n" nodes away from head pointer

    for i in range(n-1):
        if not right_pointer.nextnode:
            raise LookupError("Error: n is larger than the linked list!")

        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer

n_last = nth_to_last_node(1,node0)
print(n_last)
