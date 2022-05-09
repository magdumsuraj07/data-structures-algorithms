def isSafe(graph, colors, vertex, color):
    for i in range(len(graph)):
        if graph[vertex][i] and colors[i] == color:
            return False
    return True


# Function to determine if graph can be coloured with at most M colours such
# that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    # Array to store which has which color
    colors = [-1 for i in range(V)]

    # Recurcive function to check coloring is possible
    def backtrack(vertex):
        if vertex == V:
            return True

        # Try each and every color for every node
        for color in range(k):
            if isSafe(graph, colors, vertex, color):
                colors[vertex] = color
                if backtrack(vertex + 1):
                    return True
                colors[vertex] = -1

        return False

    return backtrack(0)
