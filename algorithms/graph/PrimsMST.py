from sys import maxsize as MAX_INT


def findMinimumVertex(weights, visited):
    minVertex = None
    for i in range(len(weights)):
        if (visited[i] is False):
            if (minVertex is None or weights[i] < weights[minVertex]):
                minVertex = i
    return minVertex


def prim(adjMatrix, nVertices):
    '''
    Implementation of prim's algorithm for finding MST(Minimum Spanning Tree)
    '''
    visited = [False for i in range(nVertices)]
    weights = [MAX_INT for i in range(nVertices)]
    parents = [-1 for i in range(nVertices)]

    weights[0] = 0
    for i in range(nVertices):
        v = findMinimumVertex(weights, visited)
        visited[v] = True
        for j in range(nVertices):
            if (adjMatrix[v][j] > 0 and visited[j] is False):
                if (adjMatrix[v][j] < weights[j]):
                    weights[j] = adjMatrix[v][j]
                    parents[j] = v

    mstEdges = []
    for i in range(1, len(parents)):
        src, dest = min(i, parents[i]), max(i, parents[i])
        weight = adjMatrix[src][dest]
        mstEdges.append((src, dest, weight))

    return mstEdges
