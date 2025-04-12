# Data Structures Tutorial

## Introduction
This tutorial will guide you through using each data structure in this package.

### Basic Operations
# Array Operations
```python
from data_structures import Array

# Create and use array
array = Array()
array.insert(5)
```
# Linkedlist Operations
```python
from data_structures import LinkedList

# Create linked list
ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtEnd(2)
ll.insertAfter(3, 0)  # Insert 3 after index 0
ll.traverse()         # Print all elements
```
# Tree Operations
```python
from data_structures import BinarySearchTree

# Create BST
bst = BinarySearchTree()
bst.insert(5)         # Add root
bst.insert(3)         # Add left child
bst.insert(7)         # Add right child
bst.inorder_traversal()  # Print sorted elements

```
# Queue Operations
```python
from data_structures import Queue
# Create queue
queue = Queue()
queue.enqueue(1)      # Add element
queue.enqueue(2)
print(queue.peek())   # View front element
queue.dequeue()       # Remove front element
```


# Stack Operations
```python
from data_structures import Stack

# Create stack
stack = Stack()
stack.push(1)         # Add element
stack.push(2)
print(stack.peek())   # View top element
stack.pop()           # Remove top element
```

### Visualizations
Each data structure includes visualization capabilities:
# Array visualization
```python
from data_structures import Array
# Array visualization
array = Array()
array.insert(5)
array.visualize() 
```

# LinkedList visualization
```python 
from data_structures import LinkedList
ll = LinkedList()
ll.insertAtBeginning(1)
ll.visualize()
```

# Queue visualization
from data_structures import queue
```python
queue = Queue()
queue.enqueue(1)
queue.visualize()
```

# Stack visualization
```python
from data_structures import Stack
stack = Stack()
stack.push(1)
stack.visualize()
```
# Tree visualization
```python
from data_structures import BinarySearchTree
bst = BinarySearchTree()
bst.insert(5)
bst.visualize()
```
