from linked_list_node import Node, print_linked_list


def remove_duplicates(head: Node):
    '''
        Remove duplicates from sorted Linked List by checking value of the next
        Node and skipping it if needed
    '''
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip duplicate
            current.next = current.next.next
        else:
            current = current.next
    return head


# Create Linked List with duplicates
linked_list = Node(1, Node(1, Node(1, Node(2, Node(3, Node(3))))))
print_linked_list(linked_list)

# Remove duplicates
linked_list = remove_duplicates(linked_list)
print_linked_list(linked_list)
