from node import Node
from matplotlib import pyplot as plt
import numpy as np

class binary_tree:

    def __init__(self, head:Node):

        self.head = head
        self.count = 0

    def add_node(self, new_node:Node):
        #adds a new node to the current tree
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                #when the users tries to add a node that already exists
                raise ValueError(f"a node with value {new_node.value} already exists in the tree.")
            elif new_node.value < current_node.value:
                if current_node.left: #i.e. if there is already a node on the left
                    current_node = current_node.left
                else: #when there is no other node on the left
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
        self.count += 1
    
    def find(self, value:int):
        #finds a node in the tree with the selected value, then print out its __repr__
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise LookupError(f"a node with value {value} was not found")

    def in_order(self):
        #traverses through the tree in order and prints out the node values
        self._in_order_recursive(self.head)

    def _in_order_recursive(self, current_node):

        if not current_node:
            return
        self._in_order_recursive(current_node.left)
        print(current_node)
        self._in_order_recursive(current_node.right)

    def pre_order(self):
        #traverses through the tree pre-order and prints out the node values
        self._pre_order_recursive(self.head)

    def _pre_order_recursive(self, current_node):

        if not current_node:
            return
        print(current_node)
        self._pre_order_recursive(current_node.left)
        self._pre_order_recursive(current_node.right)
    
    def find_parent(self, value:int) -> Node:

        if self.head and self.head.value == value: 
            return self.head

        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or\
                (current_node.right and current_node.right.value == value): 
                #meaning that we are AT the parent that we are looking for
                return current_node #*returns the children, NOT the parent
            elif value > current_node.value:
                current_node = current_node.right #go seek out higher values
            elif value < current_node.value:
                current_node = current_node.left #go seek out lower values
        #* special case: the parent of the ROOT node of the tree is the ROOT itself

    def find_rightmost(self, node:Node) -> Node:

        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node #travels right until we hit and end 

    def delete(self, value:int):

        to_delete = self.find(value) #locates the node to delete
        parent_of_to_delete = self.find_parent(value) #locates the parent of the node to delete
        
        if to_delete.left and to_delete.right:
            #the node to be deleted has TWO children
            rightmost = self.find_rightmost(to_delete.left) #locates the rightmost node on the LEFT of to_delete
            rightmost_parent = self.find_parent(rightmost.value) #locates the parent of that

            if rightmost_parent != to_delete: #i.e. to_delete deoes NOT have only ONE left node
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
            rightmost.right = to_delete.right #to reconnect nodes

            if to_delete == parent_of_to_delete.left: #to_delete is a left node
                parent_of_to_delete.left = rightmost
            elif to_delete == parent_of_to_delete.right: #to_delete is a right node
                parent_of_to_delete.right = rightmost #restructures the tree
            else:
                self.head = rightmost

        elif to_delete.left or to_delete.right: #the node to be deleted has ONE child
            if to_delete == parent_of_to_delete.left:
                parent_of_to_delete.left = to_delete.left or to_delete.right
                #we want the parent to point to the child of to_delete,
                #so we can get rid of to_delete, 
                #but we don't know if the child of to_delete
                #is on its left or on its right, hence the "or"
            elif to_delete == parent_of_to_delete.right:
                parent_of_to_delete.right = to_delete.left or to_delete.right
            else: #* special case: when to_delete is the ROOT node of the tree
                self.head = to_delete.left or to_delete.right
                
        else: #the node to be deleted has ZERO child
            if to_delete == parent_of_to_delete.left:
                parent_of_to_delete.left = None
            elif to_delete == parent_of_to_delete.right:
                parent_of_to_delete.right = None
            #deleting a node means setting its value to None 
            else:
                #* special case, triggered when to_delete is the ROOT node of the tree, 
                #* AND when the root node has ZERO child
                self.head = None #resets the entire tree
        
        self.count -= 1

    def display(self):
        pass

    def depth(self):
        return int(np.log2(self.count))+1

    def depth_of_node(self, index):
        return int(np.log2(index))+1
