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



    def append(self,value):
        """
        append method :
        arguments: new value
        Output :adds a new node with the given value to the end of the list
        """
        new_node=Node(value)
        if not self.head:
          self.head=new_node
        else:
          current_Node=self.head
          while current_Node.next !=None:
            current_Node=current_Node.next
          current_Node.next=new_node

    def insert_before(self,value,new_value):
      """
      insert_before method :
      arguments: value, new value
      adds a new node with the given new value immediately before the first node that has the value specified
      """
      new_node=Node(new_value)
      if not self.includes(value): # edge case if there is no value in the Linked list
        return f"No {value} Founded"
      elif self.head.value ==value: # edge case , if the value is in the head node
        self.insert(new_value)
      else:
        current_Node=self.head
        while current_Node.next !=None:
          if current_Node.next.value ==value:
              new_node.next=current_Node.next
              current_Node.next=new_node
              break
          current_Node=current_Node.next



    def insert_after(self,value,new_value):
      """
      insert_after method :
      arguments: value, new value
      adds a new node with the given new value immediately after the first node that has the value specified
      """
      new_node=Node(new_value)
      if not self.includes(value):
        return "No Value"
      else:
        current_Node=self.head
        while current_Node.next !=None:
          if current_Node.value == value:
            new_node.next=current_Node.next
            current_Node.next=new_node
            break
          current_Node=current_Node.next

    def __str__(self):
        """
        to string : fun with no arguments , used to print a string with all the values in the linked list

        Arguments: none
        Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        """
        current_Node= self.head
        linked_list_values=''
        while current_Node !=None:
            linked_list_values += f"{current_Node.value} -> "
            current_Node = current_Node.next
        linked_list_values+= "NULL"
        return linked_list_values

