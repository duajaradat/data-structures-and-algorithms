from stacks_queues.stacks_queues import Stack

def test_stack_push():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek()==2
