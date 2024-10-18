from trees.helper import create_bst


def search_bst(root, value):
    '''
        Binary Tree Search is efficient because we can leverage the Tree
        Structure where left node has a lower value than the root value. So
        with each step we chop off half of the remainer cases.
    '''
    # Base case
    if not root or root.value == value:
        return root
    if value < root.value:
        # If value is lower than current root.value search left Node
        return search_bst(root.left, value)
    else:
        # Otherwise search right Node
        return search_bst(root.right, value)
    

if __name__ == '__main__':
    # Example usage
    bst = create_bst()
    print(search_bst(bst, 2))
