from node import Node
from binary_tree import binary_tree
import random

tree = binary_tree(head=Node(15))
nodes = [1, 2, 3, 5, 7, 12, 19, 23, 29, 31, 37, 41]
random.shuffle(nodes)
print(nodes)

for node in nodes:
    tree.add_node(Node(node))
    #print(tree.depth())

#for node in tree.head:
#    print(node)

print("in order traversal")
tree.in_order()
print("----------")
print("pre order traversal")
tree.pre_order()
print("----------")

#tree.delete(37)
#nodes.remove(37)
#print(tree.count)

#print("new tree: ")
#tree.in_order()
