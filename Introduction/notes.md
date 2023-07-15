## Graph Theory

The mathematical theory of the properties and applications of graphs (networks).

**Graph Types**:
    
    a. Undirected Graph - A graph in which edges have no orientation. The edge (u, v) is identical to the edge (v, u). 
    ![image](https://github.com/R-J2000/Data-Structures/assets/136933973/0f8a1f86-3ba3-4629-82ea-5f44986c62a8)
    b. Directed Graph (diagraph) - A graph in which edges have orientations. For example, the edge (u, v) is the edge from node u to node v. 
        [See Attached Illustration] 
    c. Weighted Graph - Graphs–directed or undirected–where each edge has a certain weight (that represents an arbitrary 
        value such as mass, cost, distance etc.) [See Attached Illustration] 
    d. Trees - An undirected graph with no cycles or a graph with N nodes with N-1 edges. [See Attached Illustration] 
    e. Rooted Tree - A type of tree with a “root.” All other nodes either point away from a root (out-tree or arborescence) 
        or point towards it (in-tree or anti-arborescence). [See Attached Illustration] 
    f. Directed Acyclic Graphs (DAGs) - A directed graph with no cycles. Note: All out-trees are DAGs, but not all DAGs are out-trees. 
        [See Attached Illustration] 
    g. Bipartite Graph - A graph whose nodes can be divided into two groups, such that all connecting edges link nodes in one group to 
        another. Alternatively put, no edge connects nodes to another node in its own group. [See Attached Illustration] 
    h. Complete Graph - A graph where each node is directed connected to every other node. A graph is referred to as the graph Kn i
        f it is a complete graph with n nodes. [See Attached Illustration] 
        
**Representing Graphs:**

    a. Adjacency Matrix - A matrix M whose cell M[i][j] represents the edge weight of the node going from i to node j. [See Attached Illustration].
        Advantages of Adjacency Matrices:
            Space efficient for representing dense graphs
            Edge Weight lookup is O(1)
            Simple to implement
        Disadvantages of Adjacency Matrices:
            Requires O(V^2) space
            Iterating over all edges takes O(V^2) time

    b. Adjacency List - Each node is designated a list that keeps track of all the nodes it points to and the edge weights of said links. 
    [See Attached Illustration] 
        Advantages of Adjacency Lists:
            Space efficient in representing sparse graphs
            Iterating over all edges is efficient
        Disadvantages of Adjacency Lists:
            Less space efficient for denser graphs
            Edge Weight Lookup is O(E)
            More complex implementation

    c. Edge List - A way to represent a list using an unordered list of edges. Assume the notation for any triplet (u, v, w) means: 
    “The cost from node u to v is w.” Note: This representation is rarely used due it is lack of structure, but is applicable for 
    a handful of algorithms. [See Attached Illustration] 
        Advantages of Edge Lists:
            Space efficient in representing sparse graphs
            Iterating over all edges is efficient
            Simple Structure
        Disadvantages of Edge Lists:
            Less space efficient for denser graphs
            Edge Weight Lookup is O(E)


**Common Graph Theory Problems**:

    a. Shortest Path Problem - Given a weighted graph, find the shortest path of edges from initial node to end node. [See Attached Illustration]
    b. Connectivity - Does there exist a path between node A and node B
    c. Negative Cycles - Does a weighted directed graph have negative cycles (cyclic paths in the graph with total edge weight less than 0). 
        [See Attached Illustration]
    d. Strongly Connected Components - Self-contained cycles in a directed graph, where each node of the given cycle can reach every 
        other component. [See Attached Illustration]
    e. Traveling Salesman Problem - Given a list of cities and distances between each pair of cities, find the shortest possible path 
        such that a salesman can visit each city exactly once and return to the origin city. [See Attached Illustration]
    f. Bridges - An edge in the graph whose removal would increase the number of connected components (independent islands of nodes). 
        [See Attached Illustration]
    g. Articulation Point -  A node in the graph whose removal would increase the number of connected components 
        (independent islands of nodes). [See Attached Illustration]
    h. Minimum Spanning Tree (MST) - A subset of edges of a connected, edge-weight graph that connects all the nodes without any 
        cycles and with the minimum possible edge weight. [See Attached Illustration]
    i. Network Flow: Max Flow - Find the max flow through an edge-weighted graph with a source and sink. [See Attached Illustration]


