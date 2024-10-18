# Overview

A tree is a non-linear data structure consisting of nodes, where each node contains a value and references to its child nodes. The tree starts with a root node, and each node can have 0 or more child nodes. A tree does not contain cycles (i.e., it’s a directed acyclic graph).

## Basic Terminology

* Root: The topmost node in the tree.
* Parent: A node that points to child nodes.
* Child: A node that has a parent node.
* Leaf: A node that has no children.
* Subtree: A tree formed by any node and its descendants.
* Depth: The number of edges from the root to a node.
* Height: The number of edges on the longest path from the node to a leaf.

## Types of Trees

### Binary Tree
A binary tree is a tree where each node has at most two children (referred to as the left and right child).

### Binary Search Tree (BST)
A binary search tree (BST) is a binary tree where:

* The left subtree contains only nodes with values less than the parent node.
* The right subtree contains only nodes with values greater than the parent node.

### Balanced Trees
Balanced trees, such as AVL or Red-Black Trees, are BSTs that automatically keep the height balanced, ensuring that operations (insert, delete, search) remain efficient (logarithmic time complexity).

### Heap
A heap is a special tree-based data structure that satisfies the heap property:

* In a max heap, the value of a parent node is greater than or equal to the values of its children.
* In a min heap, the value of a parent node is less than or equal to the values of its children.

###  Trie (Prefix Tree)
A trie is a tree-like data structure used to store strings, where each node represents a character of the string. It's mainly used for string searching, like in autocomplete systems.

# Tree operations

For Tree operations we will use Classes and Functions available in the [helper.py](/trees/helper.py) script.

Currently covered Tree operations are:
* Traversals: [traversals.py](/trees/traversals.py)
* Insert into BST: [insert_bst.py](/trees/insert_bst.py)