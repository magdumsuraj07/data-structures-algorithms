from queue import Queue


class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for c in range(nVertices)] for r in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.containsEdge(v1, v2) is False:
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def containsEdge(self, v1, v2):
        return self.adjMatrix[v1][v2] == 1

    def __dfsHelper(self, startVertex, visited):
        print(startVertex)
        visited[startVertex] = True
        for i in range(self.nVertices):
            if self.containsEdge(startVertex, i) and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __bfsHelper(self, startVertex, visited):
        q = Queue()
        q.put(startVertex)
        visited[startVertex] = True
        while q.empty() is False:
            vertex = q.get()
            print(vertex)
            for i in range(self.nVertices):
                if self.containsEdge(vertex, i) and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)

    def __str__(self) -> str:
        return str(self.adjMatrix)
