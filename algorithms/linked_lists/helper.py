class Node:
    """
        Node class representation of singly-linked node.
    """
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def create_linked_list(length: int = 5):
    """
        Helper function used in the exercises for faster creating of five
        elements Linked List
    """
    # Instantiate nodes
    head = Node(1)
    previous_node = head
    for node in range(2, length + 1):
        new_node = Node(node)
        previous_node.next = new_node
        previous_node = new_node

    return head


def print_linked_list(head: Node):
    """
        Helper function for printing linked list
    """
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
