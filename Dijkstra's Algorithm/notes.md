#### Dijkstra's Shortest Path Algorithim

    a. Dijkstra's Algorithm starts at the node that you choose (the source node) and it analyzes the graph to find the shortest 
        path between that node and all the other nodes in the graph. 
    b. The algorithm keeps track of the currently known shortest distance from each node to the source node and it updates these 
        values if it finds a shorter path. This is done using a priority queue, which usually stores the (node index, distance) as the
        (key, value) pairs.
    c. Once the algorithm has found the shortest path between the source node and another node, that node is marked as "visited" 
        and added to the path.
    d. The process continues until all the nodes in the graph have been added to the path. This way, we have a path that connects 
        the source node to all other nodes following the shortest path possible to reach each node.

Time Complexity - Dijkstra's time complexity is typically O(Elog(V)) depending on the data structures being deployed

Requirements

    Dijkstra's Algorithm can only work with graphs that have positive weights. This is because, during the process, 
    the weights of the edges have to be added to find the shortest path.

    If there is a negative weight in the graph, then the algorithm will not work properly. Once a node has been marked as "visited", 
    the current path to that node is marked as the shortest path to reach that node. And negative weights can alter this if the total
    weight can be decremented after this step has occurred.

**Lazy vs Eager Implementation**

    The Dijkstra's can be implemented in a lazy and eager way. In the lazy approach, we use a PQ and delete the sub-optimal routes--in 
    particular duplicate key-value pairs--when they are encounter in the queue. Such is not the case for the Eager appraoch. In the 
    Eager approach we usually use an indexed priority queue. NO DUPLICATE key-value pairs are generated, the new better distance is updated
    in-place.
    
*D-ary Heap* - When executing Dijkstra's algorithim, there are a lot more updates than removals. Using D-ary heaps, allow us to update cheaply, whilst making removals more expensive. In general, the optimal D-ary heap degree D is given by E/V

