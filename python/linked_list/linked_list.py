class Node:
    """
    Put docstring here
    """

    def __init__(self,value=None,next=None):
        """
        Node class has a value that stored the Node and pointer to the next node
        """
        self.value = value
        self.next = next


    class Linked_list():
        """
        Linked list include a head property.
        Upon instantiation, an empty Linked List should be created
        """
        def __init__(self,node=None):
            self.head = node

        def insert(self,value):
            node=Node(value)
            self.head = node



        pass
