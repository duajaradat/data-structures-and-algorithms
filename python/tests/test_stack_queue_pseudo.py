import pytest
from data_structure.stacks_queues.stack_queue_pseudo import Stack,PseudoQueue,StackEmptyException

def test_enqueue_one_value():
    pseudo=PseudoQueue()
    pseudo.enqueue("Du'a")
    actual=pseudo.stack_enqueue.top.value
    expected="Du'a"
    assert actual==expected

def test_dequeue_one_values(pseudo):
    actual=pseudo.dequeue()
    expected="a"
    assert actual == expected

def test_dequeue_an_empty_queue():
    new_pseudo=PseudoQueue()
    with pytest.raises(Exception):
        new_pseudo.dequeue()




@pytest.fixture
def pseudo():
    pseudo=PseudoQueue()
    pseudo.enqueue("a")
    pseudo.enqueue("b")
    pseudo.enqueue("c")
    return pseudo
