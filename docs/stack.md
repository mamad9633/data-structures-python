# Stack Data Structure

A Last-In-First-Out (LIFO) stack implementation with vertical visualization.

## Features
- Push elements
- Pop elements
- Peek at top element
- Check if empty
- Visualize stack state

## Usage Example
```python
from data_structures.stack import Stack

# Create stack
s = Stack()

# Push elements
s.push(1)
s.push(2)

# Visualize
s.visualize()

## API Reference
- `push(item)`: Add to top
- `pop()`: Remove from top
- `peek()`: View top element
- `is_empty()`: Check if empty
- `visualize()`: Show vertical stack visualization

## Time Complexity
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- is_empty: O(1)