#SHIELA B. DIZON
#Queues and Dequeues
#github.com/ShielaDizon
#shiela.dizon1231@gmail.com

class Queue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, contents):
        if contents not in self.queue:
            self.queue.insert(0,contents)
            return True
        return False

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        return ("Queue Empty!")

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

myQueue = Queue()
print (myQueue.enqueue(5))
print (myQueue.enqueue(6))
print (myQueue.enqueue(9))
print (myQueue.enqueue(5))
print (myQueue.enqueue(3))
print (myQueue.size())
print (myQueue.dequeue())
print (myQueue.dequeue())
print (myQueue.dequeue())
print (myQueue.dequeue())
print (myQueue.size())
print (myQueue.dequeue())