#### Prim's Minimum Spanning Tree Algorithim

Lazy Approach

    - The lazy approach is a straightforward implementation of Prim's algorithm.
    - It starts with an arbitrary vertex as the initial vertex and grows the MST one vertex at a time.
    - At each step, it considers the edges connecting the already selected MST vertices to the vertices not yet in the MST.
    - It maintains a priority queue (usually implemented using a binary heap or Fibonacci heap) to efficiently retrieve the minimum-weight edge.
    - Initially, the priority queue is populated with the edges incident to the initial vertex.
    - The algorithm repeatedly selects the minimum-weight edge from the priority queue and adds it to the MST, as long as the edge connects 
        a vertex not yet in the MST.
    - If the edge connects a vertex already in the MST, it is considered a "lazy" edge, and it is skipped.
    - The algorithm continues until all vertices are included in the MST or the priority queue becomes empty.
    - The lazy approach can include some redundant edges in the priority queue, which are later skipped, resulting in potentially slower 
        performance than the eager approach.

Eager Approach

    - The eager approach improves on the lazy approach by avoiding the inclusion of redundant edges in the priority queue.
    - Similar to the lazy approach, it starts with an arbitrary vertex as the initial vertex and grows the MST one vertex at a time.
    - At each step, instead of considering all edges connected to the already selected MST vertices, it focuses only on the edges incident 
        to the newly added vertex.
    - It maintains a data structure (e.g., an array or a heap-based structure) to keep track of the minimum-weight edge connecting each 
        vertex to the MST.
    - The algorithm updates the minimum-weight edge for each vertex whenever a shorter edge is found while expanding the MST.
    - This way, it avoids adding redundant edges to the data structure, resulting in faster performance compared to the lazy approach.
    - The eager approach is more efficient in practice and is often the preferred implementation of Prim's algorithm.
    
The Eager Prim's algorithm have a time complexity of O(E log V), where E is the number of edges and V is the number of vertices in the graph. Whilst, the lazy version has a time complexity of O(E log E) The time complexity arises from the efficient retrieval of the minimum-weight edge using a priority queue or a similar data structure.

The choice between the lazy and eager approaches depends on the specific requirements and characteristics of the graph. In most cases, the eager approach provides better performance by avoiding unnecessary operations.
