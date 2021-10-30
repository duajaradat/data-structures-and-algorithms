class Node:
    """
    Node class that has properties for the value stored in the node
    """
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Queue:
    def __init__(self,collection=[]):
        self.collection = collection

    def enqueue(self,value):

        self.collection.append(value)

    def dequeue(self):
        return self.collection.pop(0)

    def peek(self):
        if len(self.collection):
            return  True
        return False

class BinaryTree:
    def __init__(self):
        self.root = None

    def breadth(self):
        """
        breadth first search method that returns list of values that Contains
        input -> None
        return -> list
        """
        dfs_output = []
        dfs =Queue()

        dfs.enqueue(self.root)

        while dfs.peek():
            front=dfs.dequeue()
            dfs_output.append(front.data)

            if front.left :
                dfs.enqueue(front.left)
            if front.right :
                dfs.enqueue(front.right)
        return dfs_output
