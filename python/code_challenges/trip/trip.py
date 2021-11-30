from data_structure.graph.graph import Graph,Vertex,Edge

def business_trip(cities_names,graph):
    """
    function checks if there are any business trip between the given cities and how much it costs
    Arguments : list of cities_names , graph of the cities
    Returns : boolen , cost

    """
    if len(cities_names)>1:
        if (cities_names[0]in list(graph.get_nodes())) and (cities_names[1] in list(graph.get_nodes())):
            neighbors = graph.get_neighbors(cities_names[1])
            if neighbors:
                for neighbor in neighbors:
                    if cities_names[0] == neighbor.vertex:
                        return True , f"${neighbor.weight}"

                    else:
                        return False , "$0"


