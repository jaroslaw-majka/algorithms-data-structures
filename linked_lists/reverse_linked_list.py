from helper import create_five_element_list, print_linked_list, Node


def reverse_linked_list(head: Node):
    '''
        Reverses the Linked List.
    '''
    previous = None
    current = head
    while current:
        # Get next node
        next_node = current.next
        # Change the order. Previous node is now next node for current node
        current.next = previous
        # Assign `current`` node as the `previous` node for next iteration
        previous = current
        # Take the `next_node`, and assign it as `current` for the next
        # iteration
        current = next_node
    return previous


# Use helper function to create 5 element linked list
linked_list = create_five_element_list()
print_linked_list(linked_list)

# Reverse linked list and print
reversed_list = reverse_linked_list(linked_list)
print_linked_list(reversed_list)
