# Binary Search Tree Examples and Usage

## Basic Operations
```python
from data_structures import BinarySearchTree

# Initialize BST
bst = BinarySearchTree()

# Adding elements
bst.insert(5)
bst.insert(3)
bst.insert(7)

# Searching
found = bst.search(3)  # Returns True

# Traversal
bst.inorder_traversal()  # Print sorted elements

## Visualization Example
```python
# Create and populate tree
bst = BinarySearchTree()
elements = [5, 3, 7, 2, 4, 6, 8]
for e in elements:
    bst.insert(e)

# Visualize tree structure
bst.visualize()
```