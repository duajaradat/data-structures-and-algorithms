import pytest
from data_structure.stacks_queues.stack_queue_pseudo import Stack,PseudoQueue,StackEmptyException

def test_enqueue_one_value():
    pseudo=PseudoQueue()
    pseudo.enqueue("Du'a")
    actual=pseudo.stack_enqueue.top.value
    expected="Du'a"
    assert actual==expected

def test_enqueue_multi_values():
    pseudo=PseudoQueue()
    actual1=pseudo.stack_enqueue.top.value
    expected1="a"
    actual2=pseudo.stack_enqueue.top.next.value
    expected2="b"
    assert actual1==expected1
    assert actual2==expected2

@pytest.fixture
def pseudo():
    pseudo=PseudoQueue()
    pseudo.enqueue("a")
    pseudo.enqueue("b")
    pseudo.enqueue("b")
    return pseudo
