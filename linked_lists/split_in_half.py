from linked_list_node import Node, create_five_element_list, print_linked_list


def split_list(head: Node):
    '''
        Split one Linked List into two using fast, and slow pointers.

        When fast pointer reaches the end of the list, slow pointer will be in
        the middle of the List, this is where we split.
    '''
    slow, fast = head, head.next

    # Move slow pointer one step and fast pointer two steps to find the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None  # Split the list into two halves
    return head, middle


# Create Linked List
linked_list = create_five_element_list()
print_linked_list(linked_list)

# Split linked list into two lists in the middle
list_one, list_two = split_list(linked_list)
print_linked_list(list_one)
print_linked_list(list_two)
