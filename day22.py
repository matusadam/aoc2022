import re

def print_world(worldmap):
    ret = ""
    for y in range(len(worldmap)):
        for x in range(len(worldmap[0])):
            if (x,y) in visited:
                match visited[x,y]:
                    case (1,0): ret += ">"
                    case (0,-1): ret += "^"
                    case (-1,0): ret += "<"
                    case (0,1): ret += "v"
            else:
                ret += worldmap[y][x]
        ret += "\n"
    print(ret)

def run(steps, px, py, fx, fy):
    for _ in range(steps):
        if (px,py) not in visited:
            visited[px,py] = (fx,fy)
        nx, ny = (px+fx, py+fy)
        match worldmap[ny][nx]:
            case ".":
                px,py = nx,ny
            case "#":
                pass
            case " ":
                px, py = trace(px, py, fx, fy)
    return px, py, fx, fy

def trace(px, py, fx, fy):
    # Walks imaginary walk in opossite direction until hits edge of map
    # Returns position before edge hit
    tfx, tfy = (-fx, -fy)
    tpx, tpy = (px+tfx, py+tfy)
    while worldmap[tpy][tpx] != " ":
        tpx, tpy = (tpx+tfx, tpy+tfy)
    return (tpx-tfx, tpy-tfy) if worldmap[tpy-tfx][tpx-tfy] != "#" else (px,py)

worldmap, inputs = open("22").read().split("\n\n")
inputs = re.findall(r"\d+|L|R", inputs)
worldmap = worldmap.split("\n")
row_len_max = max(len(x) for x in worldmap)
for row in range(len(worldmap)):
    r = worldmap[row]
    worldmap[row] = " " + r + " "*(row_len_max-len(r)+1)
worldmap = [" "*(row_len_max + 2)] + worldmap + [" "*(row_len_max + 2)]

px, py = (worldmap[1].index("."), 1)
fx, fy = (1,0)

visited = dict()

print_world(worldmap)

for i in inputs:
    match i:
        case "R":
            fx, fy = -fy, fx
        case "L":
            fx, fy = fy, -fx
        case _:
            px, py, fx, fy = run(int(i), px, py, fx, fy)

print_world(worldmap)

result = 1000*py + 4*px
match (fx,fy):
    case (1,0):  result += 0
    case (0,-1): result += 3
    case (-1,0): result += 2
    case (0,1):  result += 1
print(px,py,fx,fy)
print(result)
