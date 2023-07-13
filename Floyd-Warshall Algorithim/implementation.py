# IMPLEMENTATION OF FLOYD WARSHALL ALGORITHIM (for reference)

def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))

    # Adding vertices individually
    for r in range(nV):
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    sol(dist)

# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end = " ")
            else:
                print(dist[p][q], end = "  ")
        print(" ")