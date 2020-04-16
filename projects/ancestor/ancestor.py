# Three steps to almost all graph problems:
## Describe in terms of graphs
### Nodes: people
### Edges: relationship

## Build our graph
###

## Choose a graph algorithm
### DFT


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = set()

    def add_edge(self, child, parent):
        self.nodes[child].add(parent)

    def get_neighbors(self, child):
        return self.nodes[child]


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):

        return len(self.stack)

def dft(graph, starting_node):
    stack = Stack()

    stack.push((starting_node, 0))
    visited = set()

    visited_pairs = set()

    while stack.size() > 0:
        current_pair = stack.pop()
        visited_pairs.add(current_pair)
        current_node = current_pair[0]
        current_distance = current_pair[1]

        if current_node not in visited:
            visited.add(current_node)

            parents = graph.get_neighbors(current_node)

            for parent in parents:
                parent_distance = current_distance + 1
                stack.push((parent, parent_distance))

    longest_distance = 0
    aged_one = -1
    for pair in visited_pairs:
        node = pair[0]
        distance = pair[1]
        if distance > longest_distance:
            longest_distance = distance
            aged_one = node
    
    return aged_one

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for parent, child in ancestors:
        graph.add_node(child)
        graph.add_node(parent)
        graph.add_edge(child, parent)

    aged_one = dft(graph, starting_node)

    return aged_one