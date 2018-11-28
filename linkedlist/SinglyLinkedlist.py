class Node(object):
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

     # O(1)
    def insertStart (self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def size1(self):
        return self.size

    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size+=1
            actualNode = actualNode.nextNode

        return size

    # O(N)
    def insertEnd(self, data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList (self):
        actualNode = self.head

        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

    def remove(self, data):
        if self.head is None:
            return
        self.size -= 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode


linkedList = LinkedList()
linkedList.insertStart(12)
linkedList.insertStart(122)
linkedList.insertStart(3)
linkedList.insertEnd(31)

linkedList.traverseList()
print("Size of the linkedlist:", linkedList.size1())

linkedList.remove(31)
linkedList.remove(12)
linkedList.remove(122)
# linkedList.remove(3)

linkedList.traverseList()
print("Size of the linkedlist:", linkedList.size1())