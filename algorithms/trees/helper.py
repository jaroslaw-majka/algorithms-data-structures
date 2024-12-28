class TreeNode:
    """
        Class representation of a Tree node.

        args:
            value: value of a Node
            left: reference to left child node
            right: reference to right child node
    """
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_bst():
    """
        Create Binary Search Tree

        Structure overview:
                4
               | |
              2   6
             | | | |
             1 3 5 7
    """
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    return root
