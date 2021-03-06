class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    #   O(log n) if the tree is balanced
    def insert_node(self, data, node):
        if data < node.data:   # data is less than the root node
            if node.left_child:     # left child is not null
                self.insert_node(data, node.left_child)  # recursive call
            else:   # left child is null
                node.left_child = Node(data)     # insert left child
        else:   # data is greater than the root node
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data)

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)
        print("%s " % node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print("Removing a leaf node...")
                del node
                return None
            if not node.left_child:
                print("Removing a node with single right child...")
                temp_node = node.right_child
                del node
                return temp_node
            elif not node.right_child:
                print("Removing a node with single left child...")
                temp_node = node.left_child;
                del node
                return temp_node
            print("Removing node with two children...")
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node


bst = BinarySearchTree()

bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.insert(1)

print("Min value:", bst.get_min_value())
print("Max value:", bst.get_max_value())
bst.remove(10)

bst.traverse()