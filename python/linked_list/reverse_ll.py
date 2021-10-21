class Node:
    """
    Node class creates instances that has attributes value stored in the node and a pointer to next node
    """
    def __init__(self,value,next=None):
        self.value = value
        self.next = next



class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        """
        insert : create a node to insert new_node at the beginning of the list
        Arguments: value
        Returns: nothing
        Adds a new node with that value to the head of the list with an O(1) Time performance.
        """
        # create a new node from Node class with value
        new_node=Node(value)

        # if the linked list is empty, add new_node to the head , if not empty then set the poiter of the new_node to the head and set the new_node to the head
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def reverse(self):
            previous=None
            current = self.head
            while current is not None:
                next=current.next
                current.next=previous
                previous=current
                current=next
            self.head=previous


if __name__ == '__main__':
    LL=LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(3)
    print(LL.reverse())
