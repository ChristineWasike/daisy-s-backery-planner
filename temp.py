from models.Stack import *
from models.Queue import *


def stacks_queues():
    stack = Stack([])
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)

    queue = Queue([])
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    stack.pop()
    stack.pop()

    queue.deque()
    return stack.pop() + queue.deque()


print(stacks_queues())
