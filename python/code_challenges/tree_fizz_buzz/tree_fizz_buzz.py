from data_structure.stacks_queues.stacks_queues import Queue

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
        queue =Queue()
        queue_output = []


        queue.enqueue(self.root)

        while not queue.isEmpty():
            front=queue.dequeue()

            for child in front.children:
                queue.enqueue(child)
            queue_output.append(front.data)
        return queue_output

def fizz_buzz(number):

    if not number % 15:
        return "FizzBuzz"
    elif not  number%3 :
        return "Fizz"
    elif not number%5:
        return "Buzz"
    else:
        return str(number)

def fizz_buzz_tree(k_ary_tree : karyTree):
    """
    function takes k-ary tree and modifies values whether or not the value of each node is divisible by 3 -> "Fizz", 5 -> "Buzz",or both ("FizzBuzz").
    Arguments: k-ary tree
    Return: new k-ary tree
    """
    if not k_ary_tree.root:
        return 'Tree is empty'

    queue = Queue()
    queue.enqueue(k_ary_tree.root)

    while not queue.isEmpty():
        front=queue.dequeue()
        front.data = fizz_buzz(front.data)
        for child in front.children:
            queue.enqueue(child)

    return k_ary_tree




