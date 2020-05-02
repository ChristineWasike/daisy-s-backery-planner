class Stack:
    def __init__(self, stack):
        self.stack = stack

    def __str__(self):
        return str(self.stack)

    """
    The time complexity of the peek method is O(1) this is because
    the pointer to the last item in the stack is stored once the 
    stack is created.
    
    The space complexity is 1 because the pointer to the last item
    in the stack is the only one being stored.
    """

    def peek(self):
        return self.stack[-1]

    """
    The time complexity of the push method is O(1) this is because 
    the item is added to the stack as the last item and hence does 
    not affect the rest of the items in the stack even in the worst 
    case scenario.
    
    The space complexity of the push method is 1 because the value 
    of the pointer to the last item in the stack is updated when an 
    item is added to the stack.   
     
    """

    def push(self, item):
        self.stack.append(item)
        return self.stack

    """
    The time complexity of the pop method is O(1) this is because 
    the last item in the stack is what is removed from the stack at 
    each given point.
    
    The space complexity of the pop method is 1 because it is only 
    the pointer to the last item in the stack that is updated. 
    """

    def pop(self):
        self.stack.pop()
        return self.stack
