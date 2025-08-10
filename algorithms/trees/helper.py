from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from algorithms.trees.helper import TreeNode


class TreeNode:
    """
        Class representation of a Tree node.

        args:
            value: value of a Node
            left: reference to left child node
            right: reference to right child node
    """
    def __init__(self, value: int = 0, left:  | None = None, right: TreeNode | None = None) -> None:
        self.value: int = value
        self.left: TreeNode | None = left
        self.right: TreeNode| None = right


def create_bst() -> TreeNode:
    """
        Create Binary Search Tree

        Structure overview:
                4
               | |
              2   6
             | | | |
             1 3 5 7
    """
    root: TreeNode = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    return root
