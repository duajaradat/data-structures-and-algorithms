from stacks_queues.stacks_queues import Stack

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
