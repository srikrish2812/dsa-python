import queue

maxHeap = queue.PriorityQueue()

# Push elements into the max heap priority queue
maxHeap.put(30)  # maxHeap = {30}
maxHeap.put(10)  # maxHeap = {30, 10}
maxHeap.put(50)  # maxHeap = {50, 30, 10}
maxHeap.put(20)  # maxHeap = {50, 30, 20, 10}

# Print the top element (element with the highest priority) without removing it
print("Top element:", maxHeap.queue[0])  # 50

# Pop the top element
maxHeap.get()

# Get the size of the max heap priority queue
print("Size of the priority queue:", maxHeap.qsize())  # 3

# Check if the priority queue is empty
if maxHeap.empty():
    print("The priority queue is empty.")
else:
    print("The priority queue is not empty.")  # Not empty

# Create a second max heap priority queue
maxHeap2 = queue.PriorityQueue()

# Swap the content of the first max heap priority queue with the second one
maxHeap2.queue = maxHeap.queue.copy()

print("After swapping, the first priority queue size:", maxHeap.qsize())  # 0
print("After swapping, the second priority queue size:", maxHeap2.qsize())  # 3
