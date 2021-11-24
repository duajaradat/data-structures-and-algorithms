import pytest
from data_structure.trees.trees import BinaryTree,Node
from tree_intersection.tree_intersection import common_values

def test_will_return_none():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    assert common_values(tree1, tree2) == None

def test_return_common_values():
    one1 = Node(42)
    two2 = Node(100)
    three3 = Node(150)
    four4 = Node(200)
    five5 = Node(250)
    six6 = Node(300)
    seven7 = Node(350)
    eight8 = Node(400)

    tree1 = BinaryTree()
    tree1.root =one1
    one1.left = two2
    one1.right = three3
    two2.left = four4
    two2.right = five5
    three3.left = six6
    three3.right = seven7
    seven7.right = eight8


    one = Node(42)
    two = Node(50)
    three = Node(70)
    four = Node(100)
    five = Node(250)
    six = Node(300)
    seven = Node(350)
    eight = Node(400)

    tree2 = BinaryTree()
    tree2.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    seven.right = eight
    assert common_values(tree1, tree2) == [42, 100, 250, 300, 350, 400]


def test_return_common_values_2():
    one1 = Node(42)
    two2 = Node(100)
    three3 = Node(150)
    four4 = Node(200)
    five5 = Node(250)
    six6 = Node(300)
    seven7 = Node(350)
    eight8 = Node(400)

    tree1 = BinaryTree()
    tree1.root =one1
    one1.left = two2
    one1.right = three3
    two2.left = four4
    two2.right = five5
    three3.left = six6
    three3.right = seven7
    seven7.right = eight8


    one = Node(42)
    two = Node(50)
    three = Node(70)
    four = Node(10)
    five = Node(30)
    six = Node(340)
    seven = Node(320)
    eight = Node(410)

    tree2 = BinaryTree()
    tree2.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    seven.right = eight
    assert common_values(tree1, tree2) == [42]

