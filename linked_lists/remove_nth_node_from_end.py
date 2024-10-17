from helper import Node, create_linked_list, print_linked_list


def remove_nth_from_end(head: Node, n: int):
    '''
        Remove n-th element from the end.
        In this operation we will use 2 pointers. One will start at the n-th
        node, and the other will start at the beginning on the Linked List.
        When first will reach the end of the Linked List we will remove the
        node that the first pointer will point at.
    '''
    dummy = Node(0, head)
    first = second = dummy

    # Move first pointer to the n + 1 Node
    for _ in range(n + 1):
        first = first.next

    # Traverse untill first reaches the end of the Linked List
    while first:
        first = first.next
        second = second.next

    # Appoint second.next to the Node 2 nodes away.
    second.next = second.next.next
    return dummy.next


# Create Linked List
linked_list = create_linked_list()
print_linked_list(linked_list)

# Remove 2nd from the end Node
linked_list = remove_nth_from_end(linked_list, 2)
print_linked_list(linked_list)
