class Node:
    """
    Node class creates instances that has attributes value stored in the node and a pointer to next node
    """
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    class linked list is sequence of nodes that are connected to each other with pointer to next node
    """
    # at intialization an empty Linked List
    def __init__(self):
        self.head=None

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
    def includes(self,value):
        """
        includes : to check if the list contains a node contains the value and return True if yes and False if no
        Arguments: value
        Returns: Boolean
        Indicates whether that value exists as a Node’s value somewhere within the list.
        """

        if not self.head:
            return False
        else:
            current_Node = self.head # to search for the value , put the pointer at the head to start the search
            while current_Node != None: # loop in list unitl the current_Node is None
                if current_Node.value == value:
                    return True
                else:
                    current_Node = current_Node.next
            return False

    def __str__(self):
        """
        to string : fun with no arguments , used to print a string with all the values in the linked list

        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        current_Node=self.head
        print(current_Node)
        linked_list_values=''
        while current_Node !=None:
            linked_list_values+=f"{current_Node} -> "
            current_Node = current_Node.next
        linked_list_values+="NULL"
        return linked_list_values

