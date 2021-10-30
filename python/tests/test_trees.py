import pytest
from data_structure.trees.trees import Node ,Queue ,BinaryTree

def test_dfs():
    node_a = Node(1)
    node_b =Node(2)
    node_c = Node(3)
    node_d = Node(4)
    node_e = Node(5)
    node_f = Node(6)
    node_a.left =node_b
    node_a.right =node_c
    node_b.left =node_d
    node_b.right =node_e
    node_c.left =node_f
    # creat instance of BinaryTree
    tree = BinaryTree()
    # define the root of tree
    tree.root = node_a

    expected = [1,2,3,4,5,6]
    actual = tree.breadth()

    assert actual == expected


