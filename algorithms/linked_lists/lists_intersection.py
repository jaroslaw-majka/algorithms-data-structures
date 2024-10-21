from helper import Node, print_linked_list


def get_intersection_node(list_one: Node, list_two: Node):
    '''
        Searches for intersection of two Linked Lists.

        Returns intersection
    '''
    a, b = list_one, list_two
    # Traverse through the linked lists, compare current value of both lists,
    # if it's the same, then Intersection is found.
    while a != b:
        a = a.next if a else list_two
        b = b.next if b else list_one
    return a


# Create 2 Linked Lists
test_one = Node(1, Node(2, Node(5, Node(6))))
# List two will intersect List One
test_two = Node(3, Node(4, test_one.next.next))

intersection = get_intersection_node(test_one, test_two)
print_linked_list(intersection)
