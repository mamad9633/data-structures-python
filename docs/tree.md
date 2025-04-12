# Binary Search Tree

A BST implementation with tree visualization.

## Features
- Insert nodes
- Search nodes
- Inorder traversal
- Tree visualization
- Balanced structure
- Efficient searching

## Usage Example
```python
from data_structures.tree import BinarySearchTree

# Create tree
bst = BinarySearchTree()

# Insert elements
bst.insert(5)
bst.insert(3)
bst.insert(7)

# Search for element
found = bst.search(3)

# Traverse tree
bst.inorder_traversal()

# Visualize
bst.visualize()

## API Reference
- `insert(data)`: Insert new node
- `search(data)`: Find node
- `inorder_traversal()`: Print inorder
- `visualize()`: Show tree structure

## Time Complexity
- Insert: O(log n)
- Search: O(log n)
- Traversal: O(n)