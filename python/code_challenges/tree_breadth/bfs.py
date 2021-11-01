from data_structure.trees.trees import BinaryTree ,BinarySearch ,Node

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



def breadth_first(tree):
        """
        breadth first search function use level search that returns list of values that Contains
        input -> tree
        return -> list
        """
        bfs_output = []
        bfs =Queue()

        bfs.enqueue(tree.root)

        while bfs.peek():
            front=bfs.dequeue()
            bfs_output.append(front.data)

            if front.left :
                bfs.enqueue(front.left)
            if front.right :
                bfs.enqueue(front.right)
        return bfs_output

