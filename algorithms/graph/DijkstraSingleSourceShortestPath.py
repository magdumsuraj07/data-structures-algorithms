from sys import maxsize as MAX_INT


def getMinimumVertex(distances, visited):
    minVertex = None
    for i in range(len(distances)):
        if (visited[i] is False):
            if minVertex is None or distances[i] < distances[minVertex]:
                minVertex = i
    return minVertex


def dijkstra(adj, nVertices, sourceVertex):
    '''
    Implementation of Dijkstra's algorithm to find
    single source shortest path
    '''
    visited = [False for i in range(nVertices)]
    distances = [MAX_INT for i in range(nVertices)]
    distances[sourceVertex] = 0

    for i in range(nVertices-1):
        # Get unvisited vertex with minimum distance
        minVertex = getMinimumVertex(distances, visited)

        # Explore all the neighbours of minVertex which are unvisited
        # and update the distanc if required
        for j in range(nVertices):
            if (adj[minVertex][j] != 0 and visited[j] is False):
                if (distances[minVertex]+adj[minVertex][j] < distances[j]):
                    distances[j] = distances[minVertex]+adj[minVertex][j]
        visited[minVertex] = True

    return distances
