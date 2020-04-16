islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4

# Graph terminology:
## Nodes: 1s
## Edges: n, s, e, w
## What is an island?: Connected Components

def get_neighbors(node, islands):
    row, col = node

    neighbors = []
    step_north = step_west = step_south = step_east = False

    if row > 0:
        step_north = row - 1

    if col > 0:
        step_west = col - 1

    if row < len(islands) - 1:
        step_south = row + 1

    if col < len(islands) - 1:
        step_east = col + 1

    if step_north is not False and islands[step_north][col]:
        neighbors.append((step_north, col))
    if step_south is not False and islands[step_south][col]:
        neighbors.append((step_south, col))
    if step_west is not False and islands[row][step_west]:
        neighbors.append((row, step_west))
    if step_east is not False and islands[row][step_east]:
        neighbors.append((row, step_east))

    return neighbors

def dft_recursive(node, visited, islands):
    if node not in visited:
        visited.add(node)

        neighbors = get_neighbors(node, islands)
        for neighbor in neighbors:
            dft_recursive(neighbor, visited, islands)

def island_counter(islands):
    visited = set()
    total_islands = 0

    # iterate accross the matrix
    for row in range(len(islands)):
        for col in range(len(islands)):
            node = (row, col)

            # when we hit a 1, if not visited, run a dft/bft
            if islands[row][col] == 1 and node not in visited:
                total_islands += 1
                # mark all nodes in our connected component aka island as visited
                dft_recursive(node, visited, islands)

    
    # increment a counter
    return total_islands