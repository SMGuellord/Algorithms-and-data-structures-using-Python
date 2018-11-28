class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        self.size += 1

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def stack_size(self):
        return self.size

    def traverse_list(self):
        if not self.head:
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(" %d" % current_node.data)
                current_node = current_node.next_node

    def pop(self):
        data = self.head.data
        self.head = self.head.next_node
        self.size -= 1
        return data

    def peek(self):
        return self.head.data


stack = Stack()

stack.push(12)
stack.push(15)
stack.push(20)

print("Stack size:", stack.stack_size())
stack.traverse_list()

print("Peeked:", stack.peek())
print("Stack size:", stack.stack_size())
print("Popped:", stack.pop())
print("Stack size:", stack.stack_size())
stack.traverse_list()

