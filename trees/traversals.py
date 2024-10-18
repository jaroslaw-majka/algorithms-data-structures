from collections import deque
from helper import create_bst


def in_order_traversal(root):
    '''
        Traverses the Tree "In order" meaning Left -> Root -> Right
    '''
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)


def pre_order_traversal(root):
    '''
        Traverses the Tree in "Pre-order" meaning Root -> Left -> Right
    '''
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    '''
        Traverses the Tree in "Post-Order" meaning Left -> Right -> Root
    '''
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")


def level_order_traversal(root):
    '''
        Traverses the Tree in level order.
        Meaning it traverses from Root, then roots childs, then childs of childs and so on.

        This method is also known as Breadth-first Search
    '''
    if not root:
        return

    # Creates a queue to traverse on. Queue works as FIFO.
    queue = deque([root])
    while queue:
        # Take the first element of the queue
        node = queue.popleft()
        # Do the operations on that element (in this case just print)
        print(node.value, end=" ")
        # Check if this Node has Child Nodes and add them to the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == '__main__':
    # Create Binary Search Tree
    bst = create_bst()

    # Example usage:
    print('In order Traversal')
    in_order_traversal(bst)

    print('\nPre-order Traversal')
    pre_order_traversal(bst)

    print('\nPost-order Traversal')
    post_order_traversal(bst)

    print('\nLevel order Traversal')
    level_order_traversal(bst)
