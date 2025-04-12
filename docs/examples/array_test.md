# Array Examples and Usage

## Basic Operations
```python
from data_structures import Array

# Initialize array
arr = Array()

# Adding elements
arr.insert(1)
arr.insert(2)
arr.insert(3)

# Accessing elements
print(arr.get(0))  # Output: 1

# Searching
index = arr.search(2)  # Output: 1

# Deleting
arr.delete(1)  # Removes element at index 1

# Create and populate array
arr = Array()
for i in range(5):
    arr.insert(i * 2)

# Visualize array state
arr.visualize()
```
