from helper import create_bst


# Create Binary Search Tree
bst = create_bst()


def in_order_traversal(root):
    '''
        Traverses the Tree "In order" meaning Left -> Root -> Right
    '''
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)


# Example usage:
print('In order Traversal')
in_order_traversal(bst)
