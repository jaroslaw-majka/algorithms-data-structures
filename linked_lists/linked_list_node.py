class Node:
    '''
        Node class representation of singly-linked node.
    '''
    def __init__(self, data):
        self.data = data
        self.next = None


def create_five_element_list():
    '''
        Helper function used in the exercises for faster creating of five
        elements Linked List
    '''
    # Instatiate nodes
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)

    # Nodes will be assigned to the next, of each previous node
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    return first_node


def print_linked_list(head):
    '''
        Helper function for printing linked list
    '''
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
