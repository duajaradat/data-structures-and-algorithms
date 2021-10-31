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
        breadth first search method use level search that returns list of values that Contains
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


    def pre_order(self):
        """
        pre_order method is one of depth first search ways input -> None
        return -> list of tree items (root , left , right)
        """
        pre_output = []

        def walk(node):
            pre_output.append(node.data)

            if node.left:
                walk(node.left)

            if node.right:
                walk(node.right)

        walk(self.root)

        return pre_output

    def in_order(self):
        """
        in_order method is one of depth first search ways input -> None
        return -> list of tree items (left ,root, right)
        """
        in_output = []

        def walk(node):

            if node.left:
                walk(node.left)

            in_output.append(node.data)

            if node.right:
                walk(node.right)

        walk(self.root)

        return in_output

    def post_order(self):
        """
        post_order method is one of depth first search ways input -> None
        return -> list of tree items (left , right ,root)
        """
        post_output = []

        def walk(node):
            if node.left:
                walk(node.left)

            if node.right:
                walk(node.right)

            post_output.append(node.data)

        walk(self.root)

        return post_output


class BinarySearch:
    def add(self,value):
        if not self.root:
            self.root = Node(value)

        else:
            def walk(node):
                if value < node.value:
                    if not node.left:
                        node.left = Node(value)
                        return
                    else:
                        walk(node.left)

                else:
                    if not node.right:
                        node.right = Node(value)
                        return
                    else:
                        walk(node.right)
            walk(self.root)
