from linked_list_node import Node, print_linked_list
from merge_sorted_lists import merge_two_sorted_lists


# Split the list into two halves
def split_list(head):
    slow, fast = head, head.next

    # Move slow pointer one step and fast pointer two steps to find the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None  # Split the list into two halves
    return head, middle


# Merge Sort function
def merge_sort(head):
    '''
        Recursive function which sorts Linked List using merge sort algorithm.
    '''
    # Base case: if head is None or there is only one node
    if not head or not head.next:
        return head

    # Step 1: Split the list into two halves
    left_half, right_half = split_list(head)

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    # Step 3: Merge the two sorted halves
    return merge_two_sorted_lists(left_sorted, right_sorted)


# Example usage:
linked_list = Node(4, Node(2, Node(1, Node(3, Node(2)))))
print("Original list:")
print_linked_list(linked_list)

# Apply merge sort
sorted_linked_list = merge_sort(linked_list)
print("Sorted list:")
print_linked_list(sorted_linked_list)
