import pytest

from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree ,karyTree,TreeNode

def test_instantiate_node():
    node = TreeNode(3)
    assert node.data == 3


