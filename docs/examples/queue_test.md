# Queue Examples and Usage

## Basic Operations
```python
from data_structures import Queue

# Initialize queue
queue = Queue()

# Adding elements (enqueue)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# View front element
front = queue.peek()  # Output: 1

# Remove element (dequeue)
removed = queue.dequeue()  # Output: 1

# Check if empty
is_empty = queue.isEmpty()  # Output: False

# Create and populate queue
queue = Queue()
for i in range(1, 4):
    queue.enqueue(i)

# Visualize queue state
queue.visualize()
```