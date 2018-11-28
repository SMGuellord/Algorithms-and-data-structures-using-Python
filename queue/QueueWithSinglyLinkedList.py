class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Queue(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, data):
        self.size += 1

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def dequeue(self):
        if not self.head:
            return
        else:
            current = self.head
            previous = None
            while current.next_node is not None:
                previous = current
                current = current.next_node

            self.size -= 1
            data = current.data
            previous.next_node = None
            return data

    def peek(self):
        if not self.head:
            return
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            return current.data

    def traverse_list(self):
        if not self.head:
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(" %d" % current_node.data)
                current_node = current_node.next_node

    def queue_size(self):
        return self.size


queue = Queue()

queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print("Queue size", queue.queue_size())
queue.traverse_list()
print("Peeked: ", queue.peek())
print("Queue size", queue.queue_size())
queue.traverse_list()

print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Queue size", queue.queue_size())
queue.traverse_list()