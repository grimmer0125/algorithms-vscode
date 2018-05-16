#!/usr/bin/env python
from __future__ import print_function
import sys
import random

class Node():
    def __init__(self):
        self.left = None
        self.right = None
        self. value = None

def random_binary_tree(number_nodes=7):
    """
    Assume the value of each nodes is also randomly generated within [0, 10].
    Ther are more than one random methods. Here it is just to be formed by
    inserting the nodes in a random order.
    """
    root_node = None
    non_degree2_list = []
    if number_nodes<=0:
        print("not valid number_nodes")
        return None
    for i in range(0, number_nodes): # [0, number_nodes)
        insert_value = random.randint(0, 10) # [0,10]
        node = Node()
        node.ith = i ## for debugging, just print to show the tree now, not for search
        node.value = insert_value
        if i == 0:
            root_node = node
            print("root (0th) node's value:{}".format(insert_value))
        else:
            parent_index = random.randint(0, len(non_degree2_list)-1)
            parent = non_degree2_list[parent_index]
            isLeft = True ## for debugging
            if parent.left == None and parent.right == None:
                if random.randint(0,1) == 1:
                    parent.right = node
                    isLeft = False
                else:
                    parent.left = node
            elif parent.left == None:
                parent.left = node
                non_degree2_list.pop(parent_index)
            else:
                parent.right = node
                non_degree2_list.pop(parent_index)
                isLeft = False
            if isLeft == True:
                print("add {}th node:{} as Parent({}th)'s left".format(i, node.value, parent.ith))
            else:
                print("add {}th node:{} as Parent({}th)'s right".format(i, node.value, parent.ith))
        non_degree2_list.append(node)
    return root_node

def loop_depth_print(node):
    print("loop_depth_print")
    if node == None:
        print("invalid root node")
    print("({})".format(node.value))
    last_level_list = []
    current_level_list = []
    last_level_list.append(node)
    while True>0:
        for node in last_level_list:
            if node.left != None:
                print("({})".format(node.left.value), end='')
                current_level_list.append(node.left)
            if node.right != None:
                print("({})".format(node.right.value), end='')
                current_level_list.append(node.right)
        last_level_list = current_level_list
        current_level_list = []
        if len(last_level_list)>0:
            print("")
        else:
            break
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        node = random_binary_tree(int(sys.argv[1]))
        loop_depth_print(node)
