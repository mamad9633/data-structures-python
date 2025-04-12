# Python Data Structures Documentation

A comprehensive implementation of fundamental data structures with visualization capabilities.

## Available Data Structures

### Array
- Dynamic array implementation
- Efficient random access
- Visualization using bar charts
- [Learn more about Array](array.md)
- [View Examples & Visualizations](examples/array_examples.ipynb)

### Linked List
- Singly linked list implementation
- Dynamic memory allocation
- Node-based visualization
- [Learn more about Linked List](linkedlist.md)
- [View Examples & Visualizations](examples/linkedlist_examples.ipynb)

### Queue
- FIFO (First-In-First-Out) implementation
- Dynamic sizing
- Queue state visualization
- [Learn more about Queue](queue.md)
- [View Examples & Visualizations](examples/queue_examples.ipynb)

### Stack
- LIFO (Last-In-First-Out) implementation
- Vertical stack visualization
- Memory efficient
- [Learn more about Stack](stack.md)
- [View Examples & Visualizations](examples/stack_examples.ipynb)

### Binary Search Tree
- Ordered data structure
- Efficient searching
- Tree structure visualization
- [Learn more about Binary Search Tree](tree.md)
- [View Examples & Visualizations](examples/tree_examples.ipynb)

## Features
- Type hints for all implementations
- Comprehensive API documentation
- Time complexity analysis
- Interactive visualizations
- Example usage for each structure

## Getting Started

```python
# Import the required data structure
from data_structures import Array, LinkedList, Queue, Stack, BinarySearchTree
```
# Create instances

```python
array = Array()
linked_list = LinkedList()
queue = Queue()
stack = Stack()
tree = BinarySearchTree()
```
# Use the data structures
```python
array.insert(5)
linked_list.insertAtBeginning(1)
queue.enqueue(10)
stack.push(15)
tree.insert(20)
```
# Visualize
```python
array.visualize()
```