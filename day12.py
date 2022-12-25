import networkx as nx
import matplotlib.pyplot as plt

grid = open("12").read().split("\n")

graph = nx.DiGraph()

height = len(grid)
width = len(grid[0])
start_node = None
end_node = None
possible_start = []

for row in range(height):
    for col in range(width):
        graph.add_node(row*width + col)
        if grid[row][col] == "S":
            start_node = row*width + col
            grid[row] = grid[row].replace("S", "a")
        elif grid[row][col] == "E":
            end_node = row*width + col
            grid[row] = grid[row].replace("E", "z")
        if grid[row][col] == "a":
            possible_start.append(row*width + col)

for row in range(height):
    for col in range(width):
        curr = grid[row][col]
        # Up
        if row > 0 and ord(grid[row-1][col]) <= ord(curr) + 1:
            graph.add_edge( row*width + col, (row-1)*width + col )
        # Down
        if row < height-1 and ord(grid[row+1][col]) <= ord(curr) + 1:
            graph.add_edge( row*width + col, (row+1)*width + col )
        # Left
        if col > 0 and ord(grid[row][col-1]) <= ord(curr) + 1:
            graph.add_edge( row*width + col, (row)*width + col-1 )
        # Right
        if col < width-1 and ord(grid[row][col+1]) <= ord(curr) + 1:
            graph.add_edge( row*width + col, (row)*width + col+1 )

# Part 1
print(len(nx.shortest_path(graph, source=start_node, target=end_node))-1)

# Part 2
shortest = 100000000
for n in possible_start:
    try:
        n_len = len(nx.shortest_path(graph, source=n, target=end_node))-1
    except nx.exception.NetworkXNoPath:
        n_len = 100000000
    shortest = min(n_len, shortest)
print(shortest)