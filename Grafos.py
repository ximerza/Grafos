class EdgeListGraph:
    def __init__(self):
        self.edges = []

    def add_edge(self,u,v):
        self.edges.append((u,v))

    def remove_edge(self,u,v):
        try:
            self.edges.remove((u,v))
        except ValueError:
            raise ValueError(f"No edge exists between {u} and {v}")


class AdjMatrixGraph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, src, dest, weight=1):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = weight
        else:
            raise ValueError("Index out of range")

    def remove_edge(self, src, dest):
        if 0 <= src < self.num_vertices and 0 <= dest < self.num_vertices:
            self.adj_matrix[src][dest] = 0
        else:
            raise ValueError("Index out of range")


class AdjListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self,src,dest):
        if src in self.adj_list:
            self.adj_list[src].append(dest)
        else:
            raise ValueError(f"Source vertex {src} not in graph ")

    def remove_edge(self, src, dest):
        if src in self.adj_list:
            if dest in self.adj_list[src]:
                self.adj_list[src].remove(dest)

    def dfs(self, src, visited= None, key=print):
        if not visited:
            visited = set()

        visited.add(src)
        key(src)

        for nei in self.adj_list[src]:
            if nei not in visited:
                self.dfs(nei,visited,key)


    def bfs(self, src, key=print):
      queue = [src]
      visited = set()
      while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
          visited.add(vertex)
          key(vertex)
          for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
              queue.append(neighbor)



class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def delete_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.remove(neighbor)



class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def add_edge(self, src_value, dest_value):
        if src_value in self.vertices and dest_value in self.vertices:
            src_vertex = self.vertices[src_value]
            dest_vertex = self.vertices[dest_value]
            src_vertex.add_neighbor(dest_vertex)

    def remove_edge(self, src_value, dest_value):
        if src_value in self.vertices and dest_value in self.vertices:
            src_vertex = self.vertices[src_value]
            dest_vertex = self.vertices[dest_value]
            src_vertex.delete_neighbor(dest_vertex)

