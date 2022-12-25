from collections import defaultdict

def bounding_box(elves):
    minx = min(e[0] for e in elves)
    miny = min(e[1] for e in elves)
    maxx = max(e[0] for e in elves)
    maxy = max(e[1] for e in elves)
    return minx,miny,maxx,maxy

def print_world(elves):
    ret = ""
    minx,miny,maxx,maxy = bounding_box(elves)
    for y in range(miny,maxy+1):
        for x in range(minx,maxx+1):
            if (x,y) in elves:
                ret += "#"
            else:
                ret += "."
        ret += "\n"
    print(ret)


d = open("23").read().split("\n")

elves = set()
for y,row in enumerate(d):
    for x,col in enumerate(row):
        if col == "#":
            elves.add((x,y))

operations = [
    lambda x,y,elves: (x,y-1) if not {(x+1,y-1), (x,y-1), (x-1,y-1)}.intersection(elves) else None,
    lambda x,y,elves: (x,y+1) if not {(x+1,y+1), (x,y+1), (x-1,y+1)}.intersection(elves) else None,
    lambda x,y,elves: (x-1,y) if not {(x-1,y-1), (x-1,y), (x-1,y+1)}.intersection(elves) else None,
    lambda x,y,elves: (x+1,y) if not {(x+1,y-1), (x+1,y), (x+1,y+1)}.intersection(elves) else None,
]

moved = True
round = 0
while moved:
    moved = False
    # Propose moves
    proposed = defaultdict(list)
    # print_world(elves)
    for elf in elves:
        x,y = elf
        neigh = {(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y-1),(x-1,y+1),(x+1,y-1)}
        if neigh.intersection(elves):
            for op in operations:
                prop = op(x,y,elves)
                if prop:
                    proposed[prop].append(elf)
                    break
    # Resolve moves
    for prop_pos, prop_elves in proposed.items():
        if len(prop_elves) == 1:
            moved = True
            elves.add(prop_pos)
            elves.remove(prop_elves[0])
    # Move first element to the end
    operations = operations[1:] + operations[:1]
    round += 1

minx,miny,maxx,maxy = bounding_box(elves)

# print_world(elves)
print( (maxx-minx+1)*(maxy-miny+1) - len(elves) )
print(round)