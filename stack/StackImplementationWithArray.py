class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_stack(self):
        return len(self.stack)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.size_stack())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print(stack.size_stack())
print("Peek:", stack.peek())
print(stack.size_stack())
print("Is empty?",stack.is_empty())