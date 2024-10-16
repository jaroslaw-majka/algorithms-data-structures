class LinkedList:
    '''
        Linked List class representation used as the foundation for
        most linked list operations performed in this section.
    '''
    def __init__(self):
        self.head = None

    def __repr__(self):
        '''
            Repr for better visualization and understanding purposes.
        '''
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


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
    linked_list = LinkedList()
    first_node = Node(1)
    second_node = Node(2)
    third_node = Node(3)
    fourth_node = Node(4)
    fifth_node = Node(5)

    # `first_node` will be assigned to the head, of the linked list
    linked_list.head = first_node

    # Other nodes will be assigned to the next, of each previous node
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    return linked_list
