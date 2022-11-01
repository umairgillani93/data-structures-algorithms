import os 
import json

# LinkedList implementation
class Node:
    def __init__(self, k):
        self.k= k
        self.next = None

class LinkedList:
    def __init__(self):
        self.h = None


if __name__ == '__main__':
    node1 = LinkedList()
    node1.k = Node('Modday')
    node2 = Node('Tuesday')
    node3 = Node('Wednesday')

    node1.k.next = node2
    node2.k.next.next = node3

    print(f'node1 data: {node1.h}')
    print(f'node1 next: {node1.next}')
