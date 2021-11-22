from data_structure.hash_table.hashtable import HashTable
from data_structure.trees.trees import BinaryTree,Node

def common_values(tree_one,tree_two):

    hashtable = HashTable()
    result_values = []

    if tree_one.root == None or tree_two.root == None:
        return None


    def walk_one(node):
        if node:
            if hashtable.add(str(node.data),node.data):
                    walk_one(node.left)
                    walk_one(node.right)
    walk_one(tree_one.root)

    def walk_two(node):
        if node:
            if hashtable.contains(str(node.data)):
                result_values.append(node.data)
                walk_two(node.left)
                walk_two(node.right)
    walk_two(tree_two.root)

    print(result_values)

