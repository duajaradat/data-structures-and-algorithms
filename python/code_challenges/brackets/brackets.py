from data_structure.stacks_queues .stacks_queues import Stack
def validate_brackets(string):

    """
    Arguments: string
    Return: boolean
         representing whether or not the brackets in the string are balanced
    """
    stack=Stack()
    brackets={
        '[':']',
        '(':')',
        '{':'}',
    }

    for char in string:
        if char in brackets:
            stack.push(char)
        if char in brackets.values():
            if char == stack.peek():
                stack.pop()

    if stack.isEmpty():
        return True
    else:
        return False
