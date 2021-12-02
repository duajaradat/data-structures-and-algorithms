from data_structure.graph.graph import Graph,Vertex,Edge

def business_trip(cities_names,graph):
    """
    function checks if there are any business trip between the given cities and how much it costs
    Arguments : list of cities_names , graph of the cities
    Returns : boolen , cost

    """
    trip_cost = 0
    for i , city in enumerate(cities_names):
        if i <= len(cities_names) - 2:
            neighbor_city = cities_names[i+1]

            if city not in graph._adjacency_list or neighbor_city not in graph._adjacency_list:
                return False, "$ 0"
            flag = False

            neighbors = graph.get_neighbors(city)
            for edge in neighbors:
                if edge.vertex == neighbor_city:
                    flag = True
                    trip_cost += edge.weight

            if not flag:
                return False, "$ 0"

    return True, f"${trip_cost}"
