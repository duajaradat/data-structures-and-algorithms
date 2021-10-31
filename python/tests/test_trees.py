import pytest
from data_structure.trees.trees import Node ,Queue ,BinaryTree,BinarySearch

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

def test_pre_order():
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
    tree = BinaryTree()
    tree.root =node_a
    expected = [1,2,4,5,3,6]
    actual = tree.pre_order()
    assert actual == expected

def test_in_order():
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
    tree = BinaryTree()
    tree.root = node_a
    expected = [4,2,5,1,6,3]
    actual = tree.in_order()
    assert actual == expected


def test_post_order():
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
    tree = BinaryTree()
    tree.root = node_a
    expected = [4,5,2,6,3,1]
    actual = tree.post_order()
    assert actual == expected

def test_add_value():
    tree = BinarySearch()
    tree.add(4)
    assert tree.root.data == 4

def test_contains_value():
    tree = BinarySearch()
    tree.add(4)
    tree.add(10)
    tree.add(1)
    tree.add(-1)
    tree.add(12)
    assert tree.contains(8) == False

def test_contains_value2():
    tree = BinarySearch()
    tree.add(4)
    tree.add(10)
    tree.add(1)
    tree.add(-1)
    tree.add(12)
    assert tree.contains(-1) == True


def test_max_value():
    tree = BinarySearch()
    tree.add(4)
    tree.add(10)
    tree.add(1)
    tree.add(-1)
    tree.add(12)
    assert tree.max_value() == 12
