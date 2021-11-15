class Node:
    """
    Node class that has properties for the value stored in the node
    """
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

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




class BinarySearch(BinaryTree):
    """
    BinarySearch class is a sub-class of BinaryTree contains add and contains method
    """

    def add(self,data):
        """
        Add method , adding a value to a tree
        Arguments: value
        Return: nothing
        Adds a new node with that value in the correct location in the binary search tree.
        """

        if not self.root:
            self.root = Node(data)

        else:
            def walk(node):
                if data < node.data:
                    if not node.left:
                        node.left = Node(data)
                        return
                    else:
                        walk(node.left)

                else:
                    if not node.right:
                        node.right = Node(data)
                        return
                    else:
                        walk(node.right)
            walk(self.root)

    def contains(self, data):
        """
        Contains method show if a value is in tree or not
        Argument: value
        Returns: boolean indicating whether or not the value is in the tree at least once.
        """
        if not self.root:
            return False

        else:
            def walk(node):
                if data == node.data:
                    return True

                if data > node.data:
                    if node.right:
                        return walk(node.right)
                    else:
                        return False
                else:
                    if node.left:
                        return walk(node.left)
                    else:
                        return False
            return walk(self.root)


if __name__ == '__main__':
    tree = BinaryTree()
    node1=Node(5,3,6)
    node2=Node(3,2,4)
    node3=Node(6)
    tree.root = node1
    tree.left = node2
    tree.right = node3
    print(node1.data)
    print(node1.left)
    print(tree.root.data)
    tree.pre_order()
