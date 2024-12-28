from helper import TreeNode
from traversals import in_order_traversal


def insert_into_bst(root, value):
    """
        Inserts value(s) into a Binary Search Tree.
    """
    if not root:
        return TreeNode(value)
    if value < root.value:
        # In BST Left Node contains only values lower than the root
        root.left = insert_into_bst(root.left, value)
    else:
        root.right = insert_into_bst(root.right, value)
    return root


if __name__ == '__main__':
    # Example usage
    # Create brand new BST
    print('Create new BST with passed values')
    bst = None
    tree_values = [5, 3, 8, 2, 4, 7, 9]
    for curr_value in tree_values:
        bst = insert_into_bst(bst, curr_value)
    in_order_traversal(bst)

    # Add values to an existing BST
    print('\nAdd values to an existing BST')
    bst = insert_into_bst(bst, 1)
    in_order_traversal(bst)
