# Linked List Examples and Usage

## Basic Operations
```python
from data_structures import LinkedList

# Initialize linked list
ll = LinkedList()

# Adding elements
ll.insertAtBeginning(1)
ll.insertAtEnd(3)
ll.insertAfter(2, 0)  # Insert 2 after index 0

# Searching
found = ll.search(2)  # Returns True

# Deleting
ll.deleteItem(1)  # Delete element at index 1

# Traverse list
ll.traverse()  # Print all elements

 # Create and populate linked list
ll = LinkedList()
for i in range(1, 4):
    ll.insertAtEnd(i)

# Visualize list state
ll.visualize()
```
