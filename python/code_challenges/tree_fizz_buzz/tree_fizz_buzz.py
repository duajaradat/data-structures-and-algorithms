from code_challenges.tree_breadth.bfs import Queue


class TreeNode:
    """
    Class to instanitation node
    Attribute :data , children as list
    """
    def __init__(self,data=None,children=[]):
        self.data = data
        self.children = children


class karyTree:
    def __init__(self,root=None):
        self.root = root

    def breadth_first(self):
        """
        breadth first search function use level search that returns list of values that Contains
        input -> tree
        return -> list
        """
        queue_output = []
        queue =Queue()


        queue.enqueue(self.root)

        while  queue.peek():
            front=queue.dequeue()

            for child in front.children:
                queue.enqueue(child)
            queue_output.append(front.data)
        return queue_output



def fizz_buzz_tree(k_ary_tree : karyTree):
    """
    function takes k-ary tree and modifies values whether or not the value of each node is divisible by 3 -> "Fizz", 5 -> "Buzz",or both ("FizzBuzz").
    Arguments: k-ary tree
    Return: new k-ary tree
    """
    queue = Queue()
    if not k_ary_tree.root:
        return 'Tree is empty'

    queue.enqueue(k_ary_tree.root)

    while queue.peek():
        front=queue.dequeue()

        if front.data % 5 and front.data % 3 :
            front.data = "FizzBuzz"
        elif front.data % 3 :
            front.data = "Fizz"
        elif front.data % 5 :
            front.data = "Buzz"

        for child in front.children :
            queue.enqueue(child)


    return k_ary_tree






