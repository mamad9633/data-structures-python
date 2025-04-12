# Stack Examples and Usage

## Basic Operations
```python
from data_structures import Stack

# Initialize stack
stack = Stack()

# Adding elements (push)
stack.push(1)
stack.push(2)
stack.push(3)

# View top element
top = stack.peek()  # Output: 3

# Remove element (pop)
popped = stack.pop()  # Output: 3

# Check if empty
is_empty = stack.is_empty()  # Output: False

# Create and populate stack
stack = Stack()
for i in range(1, 4):
    stack.push(i)

# Visualize stack state
stack.visualize()
```