from helper import Node, create_linked_list, print_linked_list


def rotate_right(head, k: int) -> Node:
    """
    Rotates Linked List by `k` elements from the end.

    Example:
        Given a list: 1 -> 2 -> 3 -> 4 -> 5
        Algorithm will split it into 2 lists:
            split1 = 1 -> 2 -> 3
            split2 = 4 -> 5
        And then merge so that `split2` will be at the
        start of the Linked List
        returns: 4 -> 5 -> 1 -> 2 -> 3

    """
    first = second = head

    # Move the `first` pointer to k`th element
    for _ in range(k):
        first = first.next

    # Move both pointers until `first` reaches end of the list
    while first and first.next:
        first = first.next
        second = second.next

    # Decouple `second` element, and create a `new_node`
    decouple = second.next
    second.next = None
    new_node = decouple

    # Move to the end of the `new_node`, and once there attach
    # `head` as it's `next` element
    while new_node:
        if not new_node.next:
            new_node.next = head
            break
        new_node = new_node.next

    return decouple


if __name__ == '__main__':
    linked_list = create_linked_list()

    decoupled = rotate_right(linked_list, 2)
    print_linked_list(decoupled)
