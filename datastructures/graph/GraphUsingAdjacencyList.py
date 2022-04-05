from collections import defaultdict
from queue import Queue


class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.adj_list = defaultdict(list)

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def contains_edge(self, source, destination):
        return destination in self.adj_list[source]

    def remove_edge(self, source, destination):
        self.adj_list[source].remove(destination)

    def __dfs_helper(self, start_vertex, visited):
        print(start_vertex)
        visited[start_vertex] = True
        for dest in self.adj_list[start_vertex]:
            if visited[dest] is False:
                self.__dfs_helper(dest, visited)

    def dfs(self):
        visited = {}
        for source in self.adj_list.keys():
            visited[source] = False

        for source in self.adj_list.keys():
            if visited[source] is False:
                self.__dfs_helper(source, visited)

    def __bfs_helper(self, start_vertex, visited):
        q = Queue()
        q.put(start_vertex)
        visited[start_vertex] = True

        while q:
            vertex = q.get()
            print(vertex)
            for dest in self.adj_list[vertex]:
                if visited[dest] is False:
                    q.put(dest)
                    visited[dest] = True

    def bfs(self):
        visited = {}
        for source in self.adj_list.keys():
            visited[source] = False

        for source in self.adj_list.keys():
            if visited[source] is False:
                self.__bfs_helper(source, visited)
