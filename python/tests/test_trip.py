import pytest
from code_challenges.trip.trip import business_trip
from data_structure.graph.graph import Graph,Vertex

def test_trip_no_neighbors():
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
    graph.add_edge(pandora , arendelle ,150)
    graph.add_edge(pandora , metroville,82)

    graph.add_edge(arendelle , pandora,150)
    graph.add_edge(arendelle , metroville,99)
    graph.add_edge(arendelle , monstroplolis,42)
    graph.add_edge(metroville , naboo,26)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,monstroplolis,105)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(narnia,metroville,37)
    graph.add_edge(naboo,narnia,250)
    graph.add_edge(monstroplolis,metroville,105)
    graph.add_edge(narnia,naboo,250)
    graph.add_edge(monstroplolis,arendelle,42)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,monstroplolis,73)
    actual = business_trip([pandora,naboo],graph)
    expected = False , '$ 0'
    assert actual == expected


def test_trip_2_cities():
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
    graph.add_edge(pandora , arendelle ,150)
    graph.add_edge(pandora , metroville,82)

    graph.add_edge(arendelle , pandora,150)
    graph.add_edge(arendelle , metroville,99)
    graph.add_edge(arendelle , monstroplolis,42)
    graph.add_edge(metroville , naboo,26)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,monstroplolis,105)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(narnia,metroville,37)
    graph.add_edge(naboo,narnia,250)
    graph.add_edge(monstroplolis,metroville,105)
    graph.add_edge(narnia,naboo,250)
    graph.add_edge(monstroplolis,arendelle,42)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,monstroplolis,73)
    actual = business_trip([naboo , metroville],graph)
    expected = True , '$26'
    assert actual == expected

def test_trip_3_cities():
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
    graph.add_edge(pandora , arendelle ,150)
    graph.add_edge(pandora , metroville,82)

    graph.add_edge(arendelle , pandora,150)
    graph.add_edge(arendelle , metroville,99)
    graph.add_edge(arendelle , monstroplolis,42)
    graph.add_edge(metroville , naboo,26)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(metroville,monstroplolis,105)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(narnia,metroville,37)
    graph.add_edge(naboo,narnia,250)
    graph.add_edge(monstroplolis,metroville,105)
    graph.add_edge(narnia,naboo,250)
    graph.add_edge(monstroplolis,arendelle,42)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(naboo,monstroplolis,73)
    actual = business_trip([pandora , arendelle,monstroplolis],graph)
    expected = True , '$192'
    assert actual == expected