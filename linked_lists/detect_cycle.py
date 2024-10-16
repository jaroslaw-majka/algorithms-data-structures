from linked_list_node import create_five_element_list, Node


def has_cycle(head: Node):
    '''
        Tortoise and Hare technique.
        This function will create two pointers iterating through the list. One
        pointer will iterate on every Linked List element, while other pointer
        will make 2 node steps each iteration.
        If pointers will meet at some point, this means the node has a cycle.
    '''
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Linked List without a cycle
linked_list = create_five_element_list()
print(has_cycle(linked_list))

# Create Linked List cycle
linked_list.next.next.next.next.next = linked_list.next
print(has_cycle(linked_list))
