class TreeNode:
    '''
        Class representation of a Tree node.

        args:
            value: value of a Node
            left: reference to to left child node
            right: reference to right child node
    '''
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_bst():
    '''
        Create Binary Search Tree

        Structure overview:
            root: TreeNode(4)
                left_node (parent root): TreeNode(2) -> This node has 2 more
                nodes: TreeNode(1), TreeNode(3)
                right_node (parent root): TreeNode(6) -> This node has 2 more
                nodes: TreeNode(5), TreeNode(7)
    '''
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    return root
