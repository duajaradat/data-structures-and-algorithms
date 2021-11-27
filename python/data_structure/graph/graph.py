from data_structure.stacks_queues.stacks_queues import Queue,Stack

class Vertex:

    """
    Class for creating node for graphs
    Arguments: value
    Returns: None
    """

    def __init__(self, value=None):
        """
        Initialize the node with a value
        """
        self.value = value


class Edge:
    """
    Class for creating edges for graphs
    Arguments : node , weight
    Returns: None
    """
    def __init__(self, vertex, weight=0):
        """
        Initialize the edge with a value , and a weight if it exists(optional)
        """
        self.vertex = vertex
        self.weight = weight

class Graph:
    """

    """
    def __init__(self):
        """
        Initialize the graph
        """
        self._adjacency_list = {}


    def add_node(self,vertex):
        """
        Add a node to the graph
        Arguments: value
        Returns: vertex
        """

        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, vertex_start, vertex_end, weight=0):
        """
        Add an edge to the graph
        Arguments: vertex_start, vertex_end, weight
        Returns: None
        """
        if vertex_start not in self._adjacency_list:
            raise KeyError("vertex_start not in graph")
        if vertex_end not in self._adjacency_list:
            raise KeyError("vertex_end not in graph")

        edge = Edge(vertex_end, weight)
        adjancenies = self._adjacency_list[vertex_start]
        adjancenies.append(edge)

    def get_nodes(self):
        """
        Return all the nodes in the graph as a collection
        Arguments: None
        Returns: list of nodes
        """
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        """
        Return all the neighbors of a vertex as a collection
        Arguments: vertex
        Returns: collection of edges connected to the given vertex
        """
        return self._adjacency_list[vertex]

    def size(self):
        """
        Return the number of nodes in the graph
        Arguments: None
        Returns: number of nodes
        """
        return len(self._adjacency_list)

    def bfs(self, vertex):
        """
        Perform a breadth first search on the graph
        Arguments: vertex
        Returns: None
        """
        visited = set()
        breadth = Queue()
        nodes = []
        breadth.enqueue(vertex)
        visited.add(vertex)

        while not breadth.isEmpty() :
            front = breadth.dequeue()
            nodes.append(front.value)
            for edge in self.get_neighbors(front):
                if edge.vertex not in visited:
                    visited.add(edge.vertex)
                    breadth.enqueue(edge.vertex)


        return nodes





