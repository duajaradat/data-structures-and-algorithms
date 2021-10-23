class Node:
    def __init__(self,value):
        self.value = value
        self.next=None

class Stack:

    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    """
    def __init__(self):
        self.top=None

    def push(self,value):
        """
        push method to add new node with data at the top of stack
        """
        new_node = Node(value)
        if self.top:
            new_node.next=self.top
        self.top=new_node

    def pop(self):
        """
        pop method to remove node from the top of the stack
        """
        if not self.top:
            raise  AttributeError('Stack is empty')
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value

    def peek(self):
        """
        peek method returns the node value at the top of stack.
        """
        if self.isEmpty():
            raise AttributeError('Stack is empty')
        else:
            return self.top.value

    def isEmpty(self):
        """
        isEmpty method to check if the stack is empty or not.
        """
        if not self.top:
            return True
        else:
            return False

if __name__ == '__main__':
    stack=Stack()
    stack.peek()


