# pylint: disable=W0105
from helper import create_bst
from traversals import level_order_traversal


def delete_node(root, value):
    '''
        Deleting a node from a Binary Search Tree involves 3 cases:
        * The node is a leaf: Just remove the node.
        * The node has one child: Replace the node with its child.
        * The node has two children: Replace the node with the in-order
          successor (smallest node in the right subtree).
    '''
    # Value is not in the Tree so we return.
    if not root:
        return root

    # Recursive search of the Node that needs to be deleted
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        # Node found, this block get's executed when value == root.value

        # Node to be deleted has at most one child or no children
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        # Node with two children: Find the in-order successor
        temp = find_min(root.right)
        # After we found the successor we assign it's value as current
        # root.value
        root.value = temp.value
        # Then we delete the successor
        root.right = delete_node(root.right, temp.value)
    return root


def find_min(node):
    '''
        Helper function used for finding the successor (lowest value node)
    '''
    while node.left:
        node = node.left
    return node


if __name__ == '__main__':
    '''
        We start with tree structure looking like this
                4
               | |
              2   6
             | | | |
             1 3 5 7

        Our Algorithm is supposed to remove the value 4, so the very root of
        the tree. In such case it will search for successor in right node, and
        the new tree will look like this

                5
               | |
              2   6
             | |    |
            1   3    7
    '''
    # Example usage
    bst = create_bst()
    bst = delete_node(bst, 4)
    print('Level order traversal')
    level_order_traversal(bst)
