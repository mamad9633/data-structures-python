# Linked List Data Structure

A singly linked list implementation with node visualization.

## Features
- Insert at beginning
- Insert at end
- Insert after position
- Delete by index
- Search elements
- Traverse list
- Dynamic size
- Memory efficient

## Usage Example
```python
from data_structures.linkedlist import LinkedList

# Create list
ll = LinkedList()

# Insert elements
ll.insertAtBeginning(1)
ll.insertAtEnd(2)
ll.insertAfter(3, 1)

# Search for element
found = ll.search(2)

# Delete element
ll.deleteItem(1)

# Display list
ll.traverse()

# Visualize
ll.visualize()

## API Reference
- `insertAtBeginning(item)`: Insert at start
- `insertAtEnd(item)`: Insert at end
- `insertAfter(item, index)`: Insert after position
- `deleteItem(index)`: Delete at index
- `search(item)`: Find element
- `traverse()`: Print list
- `visualize()`: Show node connections

## Time Complexity
- Insert at beginning: O(1)
- Insert at end: O(n)
- Insert after position: O(n)
- Delete: O(n)
- Search: O(n)