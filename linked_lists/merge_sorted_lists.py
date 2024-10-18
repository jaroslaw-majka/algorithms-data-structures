from helper import Node, print_linked_list


def merge_two_sorted_lists(list_one: Node, list_two: Node):
    '''
        Merges two sorted Linked Lists into one, new sorted List.
    '''
    sorted_node = Node()
    current = sorted_node

    while list_one and list_two:
        # Assign smaller value of either `list_one` or `list_two` to the
        # current.next
        if list_one.data < list_two.data:
            current.next = list_one
            list_one = list_one.next
        else:
            current.next = list_two
            list_two = list_two.next
        # Move current to the next value
        current = current.next

    # Append remaining nodes
    current.next = list_one if list_one else list_two
    return sorted_node.next


if __name__ == '__main__':
    test_list_one = Node(1, Node(3, Node(4)))
    test_list_two = Node(1, Node(2, Node(5)))

    merged_lists = merge_two_sorted_lists(test_list_one, test_list_two)
    print_linked_list(merged_lists)
