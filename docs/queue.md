# Queue Data Structure

A Queue is a linear data structure that follows the First In First Out (FIFO) principle.

## Implementation Details

Our Queue implementation includes:
- `enqueue`: Add element to end
- `dequeue`: Remove element from front
- `peek`: View front element
- `isEmpty`: Check if queue is empty

## Visualization Example
```python
import matplotlib.pyplot as plt
import networkx as nx

def visualize_queue(queue_items):
    G = nx.Graph()
    fig, ax = plt.subplots(figsize=(10, 3))
    
    # Add nodes
    for i, item in enumerate(queue_items):
        G.add_node(i, value=item)
    
    # Add edges
    for i in range(len(queue_items)-1):
        G.add_edge(i, i+1)
    
    # Draw
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1000, ax=ax)
    
    # Add labels
    labels = {i: f"{item}" for i, item in enumerate(queue_items)}
    nx.draw_networkx_labels(G, pos, labels)
    
    plt.title("Queue Visualization")
    plt.show()
```
## API Reference
- `enqueue(item)`: Add to back
- `dequeue()`: Remove from front
- `peek()`: View front element
- `isEmpty()`: Check if empty
- `visualize()`: Show queue visualization

## Time Complexity
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- isEmpty: O(1)
