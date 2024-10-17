from linked_list_node import create_five_element_list, print_linked_list

def rotateRight(head, k: int):
    first = second = head
    for _ in range(k):
        first = first.next
    
    while first and first.next:
        first = first.next
        second = second.next

    decouple = second.next
    second.next = None
    new_node = decouple
    while new_node:
        if not new_node.next:
            new_node.next = head
            break
        new_node = new_node.next

    return decouple


head = create_five_element_list()

decoupled = rotateRight(head, 2)
print_linked_list(decoupled)
