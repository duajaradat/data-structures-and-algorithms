
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
        if self.is_empty():
            raise StackEmptyException("Empty Stack")
        else:
            return self.top.value

    def is_empty(self):
        """
        isEmpty method to check if the stack is empty or not.
        Arguments: none
        Returns: Boolean indicating whether or not the stack is empty.
        """
        if not self.top:
            return True
        else:
            return False

class PseudoQueue:
    """
    class instantiate 2 Stack instances to create and manage the queue
    """
    def __init__(self):
        self.stack_enqueue=Stack()
        self.stack_dequeue=Stack()

    def enqueue(self,value):
        """
        enqueue method to add a value to the queue
        Arguments: value
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
        self.stack_enqueue.push(value)

    def dequeue(self):
        """
        dequeue method to delete node value
        Arguments: none
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.h
        """
        if not self.stack_enqueue.peek():  # 1
            raise Exception('Empty PseudoQueue')


        while self.stack_enqueue.top:    # n  --> n*(1+1)=2n  --> Big O(n)
            popped=self.stack_enqueue.pop() # 1
            self.stack_dequeue.push(popped) # 1
        dequed=self.stack_dequeue.pop()  # 1

        while self.stack_dequeue.top:  # n  --> n*(1+1)=2n --> Big O(n)
            popped=self.stack_dequeue.pop() # 1
            self.stack_enqueue.push(popped) # 1
                                                     #

        return dequed
