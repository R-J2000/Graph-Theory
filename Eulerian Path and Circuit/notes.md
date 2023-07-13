**Eulerian Path and Circuit**

Eulerian Path - A path of edges that visits every edge exactly once. (The starting node matters)

Eulerican Circuit - An Eulerian Path that starts and ends on the same vertex (The starting node does not matter) 

Node Degree

    For undirected graphs, the degree of a node is the number of edges connected to it. It is calculated by counting the total number
        of edges that directly connect to the node. The degree of a node can be denoted as "deg(v)" or "d(v)" for a node v.

For directed graphs, the degree of a node can be further categorized into two types:

    In-Degree: The in-degree of a node in a directed graph is the number of edges directed towards that node. It represents the count 
        of incoming edges to a specific node.

    Out-Degree: The out-degree of a node in a directed graph is the number of edges originating from that node. It represents the count 
        of outgoing edges from a specific node.

For Undirected Graphs:

    Eulerian Circuit: An undirected graph has an Eulerian circuit if and only if every vertex has an even degree (the number of edges 
        incident on the vertex is even) and the graph is connected (there is a path between any pair of vertices).
    Eulerian Path: An undirected graph has an Eulerian path if and only if it is connected and has exactly two vertices with an odd degree. 
        All other vertices should have an even degree.
        
For Directed Graphs:

    Eulerian Circuit: A directed graph has an Eulerian circuit if and only if every vertex has an equal in-degree and out-degree, and the 
        graph is strongly connected (there is a directed path between any pair of vertices).
    Eulerian Path: A directed graph has an Eulerian path if and only if it is weakly connected (ignoring the direction of edges) and 
        satisfies one of the following conditions:
        a. There is exactly one vertex with out-degree minus in-degree equal to 1 (outdegree - indegree = 1), and there is exactly one 
            vertex with indegree minus outdegree equal to 1 (indegree - outdegree = 1). All other vertices should have equal in-degree 
            and out-degree.
        b. Every vertex has an equal in-degree and out-degree, except for two vertices. One vertex should have out-degree minus in-degree
            equal to 1, and the other vertex should have indegree minus out-degree equal to 1.

**Finding Eulerian Paths and Circuits**

An algorithim that can find the Eulerian Path, will give us the Circuits for free. The algorithim discussed will have a time complexity of O(E).

Eulerian Path Algorithim

    a. The find_eulerian_path function takes a graph represented as an adjacency list dictionary as input.
    b. It first calculates the degree of each vertex in the graph and stores it in the degrees dictionary.
    c. The find_start_vertex function is used to find a starting vertex for the Eulerian path. It looks for a vertex with an odd degree, 
        if one exists. Otherwise, it selects any vertex.
    d. The algorithm starts with the chosen starting vertex and initializes an empty stack and path.
    e. It iteratively selects the next neighbor for the current vertex, decrements the degrees of the current vertex and the chosen neighbor, 
        and adds the neighbor to the stack.
    f. If a vertex has no more neighbors remaining, it is removed from the stack and added to the path.
    g. Finally, the path is reversed to obtain the Eulerian path.


