from data_structure.graph.graph import Graph,Vertex,Edge

def business_trip(cities_names,graph):
    """
    function checks if there are any business trip between the given cities and how much it costs
    Arguments : list of cities_names , graph of the cities
    Returns : boolen , cost

    """
    trip_cost = 0
    for i in range(len(cities_names)-1):
        for city in graph.get_neighbors(cities_names[i]):
            if cities_names[i+1] == city[0]:
                trip_cost += city[1]
            else:
                return False , "$0"
        return True , f"$ {trip_cost}"



