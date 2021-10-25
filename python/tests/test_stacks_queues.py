import pytest
from data_structure.stacks_queues.stacks_queues import Stack,Queue,QueueEmptyException

def test_stack_push():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek()==2

def test_stack_pop():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop()==2

def test_stack_peek():
    stack=Stack()
    stack.push(1)
    stack.push(3)
    assert stack.pop()==3

def test_stack_isEmpty():
    stack=Stack()
    stack.push(1)
    stack.push(3)
    assert stack.isEmpty()==False

def test_queue_isEmpty():
    queue=Queue()
    assert queue.isEmpty()==True

def test_queue_enqueue():
    queue=Queue()
    queue.enqueue(1)
    assert queue.isEmpty()==False

def test_queue_enqueue2():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(5)
    assert queue.peek()== 1

def test_stcak_empty():
    stack2=Stack()
    with pytest.raises(Exception):
        stack2.peek()

    assert stack2.isEmpty()== 1

def test_queue_dequeue():
    queue=Queue()
    with pytest.raises(QueueEmptyException) as excinfo:
        queue.dequeue()
    assert "Empty queue" == str(excinfo.value)

def test_queue_dequeue_expected_value():
    queue3=Queue()
    queue3.enqueue(4)
    assert queue3.dequeue() == 4

def test_queue_peek():
    queue3=Queue()
    queue3.enqueue(10)
    assert queue3.peek() == 10

def test_queue_empty_after_multipule_dequeues():
    queue4=Queue()
    queue4.enqueue(10)
    queue4.enqueue(11)
    queue4.enqueue(12)
    queue4.enqueue(13)
    queue4.dequeue()
    queue4.dequeue()
    queue4.dequeue()
    queue4.dequeue()
    assert queue4.isEmpty() == True



