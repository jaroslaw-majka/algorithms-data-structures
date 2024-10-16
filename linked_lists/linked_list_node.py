class LinkedList:
    '''
        Linked List class representation used as the foundation for
        most linked list operations performed in this section.
    '''
    def __init__(self):
        self.head = None


class Node:
    '''
        Node class representation of singly-linked node.
    '''
    def __init__(self, data):
        self.data = data
        self.next = None
