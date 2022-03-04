def getParent(vertex, parents):
    if (vertex == parents[vertex]):
        return vertex
    return getParent(parents[vertex], parents)


def kruskal(edges, nVertices):
    # Sort the egdes according to ascending order of weight
    edges.sort()
    output = []
    parents = [x for x in range(nVertices)]
    edgeCount = 0
    edgeIndex = 0
    while (edgeCount < nVertices-1):
        currEdge = edges[edgeIndex]
        srcParent = getParent(currEdge.source, parents)
        destParent = getParent(currEdge.destination, parents)
        if (srcParent != destParent):
            output.append(currEdge)
            edgeCount += 1
            parents[srcParent] = destParent
        edgeIndex += 1

    return output
