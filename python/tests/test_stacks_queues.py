from stacks_queues.stacks_queues import Stack,Queue

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

def test_queue_dequeue():
    queue=Queue()
    queue.enqueue(1)

    assert queue.dequeue()==1
