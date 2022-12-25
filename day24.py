from collections import defaultdict
import random
import networkx as nx

def print_world(world, height, width):
    ret = ""
    for y in range(height+2):
        for x in range(width+2):
            if (x,y) in world:
                if len(world[x,y]) > 1:
                    ret += str(len(world[x,y]))
                else:
                    match world[x,y][0]:
                        case (1,0): ret += ">"
                        case (-1,0): ret += "<"
                        case (0,1): ret += "v"
                        case (0,-1): ret += "^"
            elif (y == 0 and x != 1) or (y == height + 1 and x != width) or x == 0 or x == width+1:
                ret += "#"
            else:
                ret += "."     
        ret += "\n"
    print(ret)

def init_world(d):
    width = len(d[0]) - 2
    height = len(d) - 2
    world = dict()
    for y,row in enumerate(d):
        for x,char in enumerate(row):
            match char:
                case "<": world[x,y] = [(-1,0)]
                case ">": world[x,y] = [(1,0)]
                case "^": world[x,y] = [(0,-1)]
                case "v": world[x,y] = [(0,1)]
    return world, width, height

def step(world, height, width):
    new_world = defaultdict(list)
    for (x,y),tile in world.items():
        for o in tile:
            vx,vy = o
            new_world[(x+vx-1)%width + 1, (y+vy-1)%height + 1].append(o)
    return new_world

def generate_layer(world, width, height, minute, G):
    nodes = list()
    for y in range(height+2):
        for x in range(width+2):
            if (x,y) not in world and not ((y == 0 and x != 1) or (y == height + 1 and x != width) or x == 0 or x == width+1):
                G.add_node((x,y,minute))
                nodes.append( (x,y) )
    return nodes

def generate_graph(d, minutes):
    G = nx.DiGraph()

    world, width, height = init_world(d)

    nodes = generate_layer(world, width, height, 0, G)
    for minute in range(1,minutes):
        world = step(world, height, width)
        nodes_next = generate_layer(world, width, height, minute, G)
        for x,y in nodes:
            if (x,y,minute) in G: G.add_edge((x,y,minute-1),(x,y,minute))
            if (x+1,y,minute) in G: G.add_edge((x,y,minute-1),(x+1,y,minute))
            if (x-1,y,minute) in G: G.add_edge((x,y,minute-1),(x-1,y,minute))
            if (x,y+1,minute) in G: G.add_edge((x,y,minute-1),(x,y+1,minute))
            if (x,y-1,minute) in G: G.add_edge((x,y,minute-1),(x,y-1,minute))
        nodes = nodes_next

    print(f"Finished building graph, node count: {len(G)}")

    for m in range(width+height, minutes):
        try:      
            path_length = nx.shortest_path_length(G, (1,0,0), (width, height+1, m))
            print(f"Reached end in {m} minutes !!!")
            break
        except nx.exception.NetworkXNoPath:
            print(f"Failed to reach end in {m} minutes")
            pass

    to_remove = set()
    for node in G:
        x,y,t = node
        if t < path_length:
            to_remove.add(node)
    for n in to_remove:
        G.remove_node(n)

    for m in range(path_length + width+height, minutes):
        try:      
            path_length += nx.shortest_path_length(G, (width, height+1, path_length), (1, 0, m))
            print(f"Back to start in {m} minutes !!!")
            break
        except nx.exception.NetworkXNoPath:
            print(f"Failed to reach back to start in {m} minutes")
            pass

    to_remove = set()
    for node in G:
        x,y,t = node
        if t < path_length:
            to_remove.add(node)
    for n in to_remove:
        G.remove_node(n)

    for m in range(path_length + width+height, minutes):
        try:      
            path_length += nx.shortest_path_length(G, (1,0,path_length), (width, height+1, m))
            print(f"Reached end again in {m} minutes !!!")
            break
        except nx.exception.NetworkXNoPath:
            print(f"Failed to reach end again in {m} minutes")
            pass

    return path_length

        
    
d = open("24").read().split("\n")


path_length = generate_graph(d, 1200)
print(path_length)

