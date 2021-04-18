class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        yield self.left
        yield self.right

    def get_children(self):
        for node in tree.head:
            yield node

    def get_children_rec(self):
        for node in tree.head:
            yield from node.get_children()


    def __repr__(self):
        return f"this node has a value of {self.value}."