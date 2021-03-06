import pytest
from data_structure.trees.trees import BinarySearch ,BinaryTree , Node
from code_challenges.tree_breadth.bfs import breadth_first

def test_bfs():
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
    actual = breadth_first(tree)

    assert actual == expected

def test_bfs_one_value_root():
    node_a =Node(90)
    # creat instance of BinaryTree
    tree = BinaryTree()
    # define the root of tree
    tree.root = node_a

    expected = [90]
    actual = breadth_first(tree)

    assert actual == expected

def test_empty_tree_edge_case():
    # creat instance of BinaryTree
    tree = BinaryTree()
    with pytest.raises(Exception):
        breadth_first()
