class Queue:
    def __init__(self, queue):
        self.queue = queue

    def __str__(self):
        return str(self.queue)

    """
    The time complexity for the peek method is O(1) this is 
    because there is a pointer to the last element in the stack.
    
    The space complexity is 1 because the pointer to the 
    last element is what's being stored. 
    """
    def peek(self):
        return self.queue[0]

    """
    The time complexity of the enqueue method in the worst case
    is O(1) this is because the last item is added to the end of 
    the queue. The other elements are not affected in this regard.
    
    The space complexity is 1 I think. This is because the value of 
    pointer to the last item is continually changed to the value of 
    the added item.      
    """
    def enqueue(self, item):
        self.queue.append(item)
        return self.queue

    """
    The time complexity of the deque method in the worst case
    is O(n) this is because the first item is removed sequentially 
    as the other elements are pushed forward.
    
    The space complexity of the deque method is n because the pointer 
    of the first item is updated each time and the remaining items in 
    the queue are pushed forward.  
    """
    def deque(self):
        self.queue.pop(0)
        return self.queue
