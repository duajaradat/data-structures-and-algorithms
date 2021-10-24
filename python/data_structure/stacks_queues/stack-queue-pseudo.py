class Node:
    """
    class to instantiate node "
    """
    def __init__(self,value):
        self.value = value
        self.next=None
class StackEmptyException(Exception):
    pass


class Stack:

    """
    Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    """
    def __init__(self):
        self.top=None

    def push(self,value):
        """
        push method to add new node with data at the top of stack
        Arguments: value
        adds a new node with that value to the top of the stack with an O(1) Time performance.
        """
        new_node = Node(value)
        if self.top:
            new_node.next=self.top
        self.top=new_node

    def pop(self):
        """
        pop method to remove node from the top of the stack
        Arguments: none
        Returns: the value from node from the top of the stack
        """
        if not self.top:
            raise StackEmptyException("Empty Stack")
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value

    def peek(self):
        """
        peek method returns the node value at the top of stack.
        Arguments: none
        Returns: Value of the node located at the top of the stack
        """
        if self.isEmpty():
            raise StackEmptyException("Empty Stack")
        else:
            return self.top.value

    def isEmpty(self):
        """
        isEmpty method to check if the stack is empty or not.
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        """
        if not self.top:
            return True
        else:
            return False
