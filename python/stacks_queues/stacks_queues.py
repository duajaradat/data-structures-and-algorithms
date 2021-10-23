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


class Queue:
    def __init__(self):
        """
        It creates an empty Queue when instantiated
        """
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """
        Arguments: value
        adds a new node with that value to the back of the queue with an O(1) Time performance.
        """
        new_node=Node(value)
        if not self.rear :
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node

    def dequeue(self):
        """
        Arguments: none
        Returns: the value from node from the front of the queue
        Removes the node from the front of the queue
        Should raise exception when called on empty queue
        """
        if self.isEmpty():
            raise AttributeError("Queue is empty")
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
        if self.front==None: # if size of queue is 1
            self.rear=None
        return temp.value
    def isEmpty(self):
        """
        Arguments: none
        Returns: Boolean indicating whether or not the queue is empty
        """
        if self.front is None and self.rear is None:
            return True
        else:
            return False
    def peek(self):
        """
        Arguments: none
        Returns: Value of the node located at the front of the queue
        Should raise exception when called on empty stack
        """
        if self.isEmpty():
            raise AttributeError("Empty queue")
        else:
            return self .front.value



if __name__ == '__main__':
    stack=Stack()
    stack.peek()


