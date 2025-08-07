from typing import Optional, Any, List
from heapq import heappop, heappush

class Graph:
    """
    Graph class
    """
    def __init__(self):
        self._graph = {}

    def add_vertex(self, vertex: str, data: Optional[Any]=None) -> None:
        """
        Adds a vertex to the graph
        :param vertex: the vertex name
        :param data: data associated with the vertex
        """
        if vertex not in self._graph:
            self._graph[vertex] = {'data': data, 'neighbors': {}}

    def add_edge(self, vertex1: str, vertex2: str, data: Optional[Any]=None) -> None:
        """
        Adds an edge to the graph
        :param vertex1: vertex1 key
        :param vertex2: vertex2 key
        :param data: the data associated with the edge
        """
        if not vertex1 in self._graph or not vertex2 in self._graph:
            raise ValueError("The vertexes do not exist")
        self._graph[vertex1]['neighbors'][vertex2] = data
        self._graph[vertex2]['neighbors'][vertex1] = data


    def get_neighbors(self, vertex) -> List[str]:
        """
        Get the list of vertex neighbors
        :param vertex: the vertex to query
        :return: the list of neighbor vertexes
        """
        if vertex in self._graph:
            return list(self._graph[vertex]['neighbors'].keys())
        else:
            return []

    def get_vertex_data(self, vertex: str) -> Optional[Any]:
        """
        Gets  vertex associated data
        :param vertex: the vertex name
        :return: the vertex data
        """
        if self.vertex_exists(vertex):
            return self._graph[vertex]['data']
        else:
            return None

    def get_edge_data(self, vertex1: str, vertex2: str) -> Optional[Any]:
        """
        Gets the vertexes edge data
        :param vertex1: the vertex1 name
        :param vertex2: the vertex2 name
        :return: vertexes edge data
        """
        if self.edge_exists(vertex1, vertex2):
            return self._graph[vertex1]['neighbors'][vertex2]
        raise ValueError("The edge does not exist")

    def vertex_exists(self, vertex: str) -> bool:
        """
        Checks if a vertex exists in the graph
        :param vertex: the vertex name
        :return: True if the vertex exists, False otherwise
        """
        return vertex in self._graph

    def edge_exists(self, vertex1: str, vertex2: str) -> bool:
        """
        Checks if an edge exists between two vertices
        :param vertex1: the first vertex name
        :param vertex2: the second vertex name
        :return: True if the edge exists, False otherwise
        """
        return vertex2 in self._graph[vertex1]['neighbors']

    def print_graph(self) -> None:
        """
        Prints the graph
        """
        for vertex, data in self._graph.items():
            print("Vertex:", vertex)
            print("Data:", data['data'])
            print("Neighbors:", data['neighbors'])
            print("")

# Inicializar el grafo con los vértices y aristas de la imagen 1
graph1 = Graph()
vertices1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
edges1 = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'F'), ('C', 'G'), ('F', 'H'), ('G', 'I')]

for vertex in vertices1:
    graph1.add_vertex(vertex)

for edge in edges1:
    graph1.add_edge(edge[0], edge[1], 1)

# Funciones para implementar
def bfs(graph: Graph, start_vertex: str) -> List[str]:
    """
    Breadth-First Search (BFS) implementation
    :param graph: The graph to search
    :param start_vertex: The starting vertex
    :return: A list of vertices in the order they were visited
    """
    pass

def dfs(graph: Graph, start_vertex: str) -> List[str]:
    """
    Depth-First Search (DFS) implementation
    :param graph: The graph to search
    :param start_vertex: The starting vertex
    :return: A list of vertices in the order they were visited
    """
    pass

# Inicializar el grafo con los vértices y aristas de la imagen 2
graph2 = Graph()
vertices2 = ['A', 'B', 'C', 'D', 'E']
edges2 = [
    ('A', 'B', 4), 
    ('A', 'C', 2), 
    ('C', 'B', 1), 
    ('C', 'D', 4), 
    ('C', 'E', 5), 
    ('B', 'C', 3),
    ('B', 'D', 2), 
    ('B', 'E', 3),
    ('E', 'D', 1)
    ]

for vertex in vertices2:
    graph2.add_vertex(vertex)

for edge in edges2:
    graph2.add_edge(edge[0], edge[1], edge[2])

# Función para implementar Dijkstra
def dijkstra(graph: Graph, start_vertex: str) -> dict:
    """
    Dijkstra's algorithm implementation
    :param graph: The graph to search
    :param start_vertex: The starting vertex
    :return: A dictionary of shortest distances from the start vertex to each other vertex
    """
    pass

def shortest_path_bfs(graph: Graph, start: str, end: str) -> List[str]:
    """
    Encuentra el camino más corto entre dos nodos usando BFS
    :param graph: El grafo para buscar
    :param start: El nodo de inicio
    :param end: El nodo de destino
    :return: Una lista de nodos en el camino más corto o un mensaje si no existe un camino
    """
    pass
    




if __name__ == "__main__":
    # Llamadas a BFS y DFS en el primer grafo
    print("BFS:", bfs(graph1, 'A'))
    print("DFS:", dfs(graph1, 'A'))

    # Llamada a Dijkstra en el segundo grafo
    print("Dijkstra:", dijkstra(graph2, 'A'))
    print("Shortest Path BFS:", shortest_path_bfs(graph1, 'A', 'I'))
