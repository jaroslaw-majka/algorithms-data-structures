from helper import create_bst


def height(root):
    '''
        Calculates the height of the tree.
        Recursive function that uses DFS to traverse the tree and with each
        iteration returns depth value
    '''
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


if __name__ == '__main__':
    bst = create_bst()
    print(height(bst))
