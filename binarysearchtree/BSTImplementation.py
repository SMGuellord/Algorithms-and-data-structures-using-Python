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
            return self.get_min()
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_man(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max()
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