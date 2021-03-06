import pytest

from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree ,karyTree,TreeNode , fizz_buzz

def test_instantiate_node():
    node = TreeNode(3)
    assert node.data == 3


def test_instantiate_empty_k_tree():
    tree = karyTree()
    assert tree.root == None

def test_instantiate_k_tree_with_root():
    node = TreeNode(3)
    tree = karyTree(node)
    assert tree.root.data == 3
    assert tree.root.children == []

def test_bfs_k_tree():
    node4 =TreeNode(4)
    node5 =TreeNode(5)
    node6 =TreeNode(6)
    node7 =TreeNode(7)
    node8 =TreeNode(8)
    node9 =TreeNode(9)
    node2=TreeNode(2,[node4,node5,node6,node7])
    node3= TreeNode(3,[node8,node9])
    node1 = TreeNode(1,[node2,node3])
    tree = karyTree(node1)
    assert tree.breadth_first() == [1,2,3,4,5,6,7,8,9]

def test_fizz(new_tree):
    fizz_buzz_tree(new_tree)
    assert new_tree.breadth_first() == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz"]

def test_fizz_buzz_fun_returns_fizz():
    expected = "Fizz"
    actual = fizz_buzz(3)

    assert actual == expected

def test_fizz_buzz_fun_returns_buzz():
    expected = "Buzz"
    actual = fizz_buzz(5)

    assert actual == expected

def test_fizz_buzz_fun_returns_fizzbuzz():
    expected = "FizzBuzz"
    actual = fizz_buzz(30)

    assert actual == expected

@pytest.fixture
def new_tree():
    node4 =TreeNode(4)
    node5 =TreeNode(5)
    node6 =TreeNode(6)
    node7 =TreeNode(7)
    node8 =TreeNode(8)
    node9 =TreeNode(9)
    node2=TreeNode(2,[node4,node5,node6,node7])
    node3= TreeNode(3,[node8,node9])
    node1 = TreeNode(1,[node2,node3])
    new_tree = karyTree(node1)
    return new_tree
