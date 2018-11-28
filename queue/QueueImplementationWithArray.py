# FIFO First in First Out
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print(queue.size_queue())
print("Dequeue: ", queue.dequeue())
print("Dequeue: ", queue.dequeue())
print("Peek: ", queue.peek())
print("Size of the queue: ", queue.size_queue())