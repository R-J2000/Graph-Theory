#### Floyd-Warshall Algorithim 

The Floyd-Warshall algorithm is a dynamic programming algorithm used to find the shortest path between all pairs of vertices in a weighted directed graph, including both negative and positive edge weights. It solves the all-pairs shortest path problem efficiently by considering all possible intermediate vertices in a recursive manner.

Here's an overview of the Floyd-Warshall algorithm:

    a. It maintains a 2D matrix, often called the "distance matrix," to store the shortest distances between pairs of vertices.
    b. The algorithm initializes the distance matrix with the direct edge weights between vertices. If there is no direct edge between 
        two vertices, the distance is set to infinity.
    c. It then iterates over all possible intermediate vertices and gradually updates the distance matrix to find shorter paths.
    d. For each vertex pair (i, j) and intermediate vertex k, the algorithm checks if the path from i to j through k yields a 
        shorter distance compared to the direct path from i to j. If so, it updates the distance matrix accordingly.
    e. After the algorithm completes, the distance matrix contains the shortest path distances between all pairs of vertices.

Use cases of the Floyd-Warshall algorithm:

    a. Finding shortest paths in a dense graph: The Floyd-Warshall algorithm is efficient for dense graphs where the number of edges is 
        close to the maximum possible number of edges.
    b. Negative edge weight graphs: Unlike Dijkstra's algorithm, the Floyd-Warshall algorithm can handle negative edge weights and 
        identify negative cycles.
    c. Traffic routing: The algorithm can be used to determine optimal routes in a transportation network, such as finding the shortest 
        path between any two cities considering various road distances or travel times.
    d. Network routing: In network routing protocols, the Floyd-Warshall algorithm can help determine the shortest paths and distances 
        between routers in a network.
    e. Graph analysis: The algorithm is useful in analyzing the connectivity and distances between nodes in a graph, providing insights 
        into the structure and relationships within a network.
        
It's worth noting that the Floyd-Warshall algorithm has a time complexity of O(V^3), where V is the number of vertices in the graph. Thus, it is more efficient for smaller graphs or graphs with a limited number of vertices. For larger graphs, other algorithms like Dijkstra's algorithm or A* search may be preferred for specific path finding between individual pairs of vertices.
