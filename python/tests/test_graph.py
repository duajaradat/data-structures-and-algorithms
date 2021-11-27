import pytest
from data_structure.graph.graph import Graph, Vertex ,Edge

def test_graph_init():
    graph = Graph()
    assert graph._adjacency_list == {}

def test_vertex_init():
    vertex = Vertex(1)
    assert vertex.value == 1

def test_edge_init():
    edge = Edge(1, 2)
    assert edge.vertex == 1
    assert edge.weight == 2

def test_graph_empty():
    graph = Graph()
    assert graph

def test_vertex_added_to_graph():
    graph = Graph()
    vertex = Vertex(1)
    graph.add_node(vertex)
    assert graph.size() == 1

def test_an_edge_added_to_graph():
    graph = Graph()
    vertex1 = Vertex(7)
    vertex2 = Vertex(4)
    graph.add_node(vertex1)
    graph.add_node(vertex2)
    graph.add_edge(vertex1, vertex2, 44)
    vertex_list = graph._adjacency_list[vertex1]
    edge = vertex_list[0]
    assert edge.vertex == vertex2
    assert edge.weight == 44

def test_get_nodes():
    graph = Graph()
    vertex_start = Vertex(1)
    vertex_end = Vertex(2)
    graph.add_node(vertex_start)
    graph.add_node(vertex_end)
    assert graph.size() == 2


def test_nodes_in_graph():
    graph = Graph()
    vertex_start = Vertex(1)
    vertex_end = Vertex(2)
    graph.add_node(vertex_start)
    graph.add_node(vertex_end)
    vertex_list = graph.get_nodes()
    assert len(vertex_list) == 2

def test_edges_in_graph():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    actual = graph.get_neighbors(v1)
    edge1 = actual[0]
    edge2 = actual[1]
    assert edge1.vertex == v2
    assert edge1.weight == 1
    assert edge2.vertex == v3
    assert edge2.weight == 2

def test_bfs_graph():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    actual = graph.bfs(v1)
    assert actual == [1, 2, 3]

