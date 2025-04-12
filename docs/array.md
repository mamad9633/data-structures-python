# Array Data Structure

A dynamic array implementation with visualization capabilities.

## Features
- Insert elements
- Delete elements by index
- Search for elements
- Get element by index
- Visualize array state

## Usage Example
```python
from data_structures.array import Array

# Create array
arr = Array()

# Insert elements
arr.insert(5)
arr.insert(10)

# Visualize
arr.visualize()
```

## API Reference
- `insert(item)`: Add element to array
- `delete(index)`: Remove element at index
- `search(item)`: Find index of item
- `get(index)`: Get element at index
- `length()`: Get array size
- `visualize()`: Show bar chart visualization

## Time Complexity
- Insert: O(1) amortized
- Delete: O(n)
- Search: O(n)
- Get: O(1)