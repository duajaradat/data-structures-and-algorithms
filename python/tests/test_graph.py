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

# BFS tests

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
    assert graph.size() == 3

def test_bfs_with_root_Pandora(bfs):
    graph = bfs[0]
    pandora=bfs[1]
    assert graph.bfs(pandora) == ["Pandora", "Arendelle","Metroville", "Monstroplolis","Narnia","Naboo"]


def test_bfs_with_root_Narina(bfs):
    graph = bfs[0]
    narnia=bfs[3]
    assert graph.bfs(narnia) == ["Narnia","Metroville","Naboo","Arendelle", "Monstroplolis","Pandora"]


# DFS tests

def test_dfs_graph_test1():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_edge(v1, v2)
    graph.add_edge(v1, v3)
    actual = graph.dfs(v1)
    assert actual == [1, 3, 2]
    assert graph.size() == 3

def test_dfs_graph_test2():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    actual = graph.dfs(v1)
    assert actual == [1]
    assert graph.size() == 3

def test_dfs_graph_test3():
    graph = Graph()
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    graph.add_node(v1)
    graph.add_node(v2)
    graph.add_node(v3)
    graph.add_edge(v2, v3)
    graph.add_edge(v1, v3)
    actual = graph.dfs(v2)
    assert actual == [2, 3]
    assert graph.size() == 3


#
@pytest.fixture
def bfs():
    graph = Graph()
    pandora = Vertex('Pandora')
    arendelle = Vertex('Arendelle')
    metroville = Vertex('Metroville')
    monstroplolis = Vertex('Monstroplolis')
    narnia = Vertex('Narnia')
    naboo = Vertex('Naboo')
    graph.add_node(pandora)
    graph.add_node(arendelle)
    graph.add_node(metroville)
    graph.add_node(monstroplolis)
    graph.add_node(narnia)
    graph.add_node(naboo)
    graph.add_edge(pandora , arendelle)

    graph.add_edge(arendelle , pandora)
    graph.add_edge(arendelle , metroville)
    graph.add_edge(arendelle,monstroplolis)

    graph.add_edge(metroville,arendelle)
    graph.add_edge(metroville,monstroplolis)
    graph.add_edge(metroville,narnia)
    graph.add_edge(metroville,naboo)

    graph.add_edge(monstroplolis,arendelle)
    graph.add_edge(monstroplolis,metroville)
    graph.add_edge(monstroplolis,naboo)

    graph.add_edge(narnia,metroville)
    graph.add_edge(narnia,naboo)

    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,monstroplolis)

    return graph,pandora,naboo,narnia,metroville,monstroplolis,arendelle

