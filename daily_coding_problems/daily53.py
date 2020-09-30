# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.

class Queue:

    def __init__(self):

        self.stackFront = []
        self.stackBack = []

    def enqueue(self, val):
        self.stackFront.append(val)
    
    def dequeue(self):
        if not self.stackBack:
            while self.stackFront:
                self.stackBack.append(self.stackFront[-1])
                del self.stackFront[-1]
        if not self.stackBack:
            raise IndexError("Queue empty")
        del self.stackBack[-1]

    def printQueue(self):
        print (f"Front {self.stackFront} Back {self.stackBack}")


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.printQueue()
q.dequeue()
q.printQueue()
q.dequeue()
q.enqueue(4)
q.printQueue()
q.dequeue()
q.dequeue()
q.dequeue()
        