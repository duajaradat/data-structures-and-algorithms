
def validate_brackets(input):

    """
    Arguments: string
    Return: boolean
         representing whether or not the brackets in the string are balanced
    """
    stack=[]
    brackets={
        '[':']',
        '(':')',
        '{':'}',
    }

    for char in input:
        if char in brackets:
            stack.append(char)
        if char in brackets.values():
            if char == brackets[stack[-1]]:
                stack.pop()

    if len(stack)==0:
        return True
    else:
        return False


if __name__ == '__main__':
    input = '{\}{Code}[Fellows](())'
    print(validate_brackets(input))
    input2='(]('
    print(validate_brackets(input2))
