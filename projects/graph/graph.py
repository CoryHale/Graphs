"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex): #Breadth First Traversal - QUEUE
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        visited = set()
        while queue.size > 0:
            cur_vert = queue.dequeue()
            if cur_vert not in visited:
                visited.add(cur_vert)
                neighbors = self.get_neighbors(cur_vert)
                for neighbor in neighbors:
                    queue.enqueue(neighbor)

        return visited

    def dft(self, starting_vertex): # Depth First Traversal - STACK
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)
        visited = set()
        while stack.size > 0:
            cur_vert = stack.pop()
            if cur_vert not in visited:
                visited.add(cur_vert)
                neighbors = self.get_neighbors(cur_vert)
                for neighbor in neighbors:
                    stack.push(neighbor)

        return visited

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if vertex not in visited:
            visited.add(vertex)
            neighbors = self.get_neighbors(vertex)
            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)

        return visited

    def bfs(self, starting_vertex, destination_vertex): # Breadth First Search - QUEUE
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        visited = set()

        path = [starting_vertex]

        queue.enqueue(path)

        while queue.size > 0:
            current_path = queue.dequeue()
            cur_vert = current_path[-1]

            if cur_vert == destination_vertex:
                return current_path

            if cur_vert not in visited:
                visited.add(cur_vert)
                neighbors = self.get_neighbors(cur_vert)

                for neighbor in neighbors:
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)



    def dfs(self, starting_vertex, destination_vertex): # Depth First Search - STACK
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()

        path = [starting_vertex]

        stack.push(path)

        while stack.size > 0:
            current_path = stack.pop()
            cur_vert = current_path[-1]

            if cur_vert == destination_vertex:
                return current_path

            if cur_vert not in visited:
                visited.add(cur_vert)
                neighbors = self.get_neighbors(cur_vert)

                for neighbor in neighbors:
                    path_copy = current_path[:]
                    path_copy.append(neighbor)
                    stack.push(path_copy)

    def dfs_recursive(self, vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if vertex not in visited:
            path.append(vertex)
            visited.add(vertex)

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4) 
    graph.add_vertex(5) 
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
