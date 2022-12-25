import re

d = [list(map(int, re.findall(r'-?\d+', row))) for row in open("15").read().split("\n")]

# Part 1
goal = 2000000
beacons_missing = set()
beacons_at_goal = set()
for sx, sy, bx, by in d:
    if by == goal:
        beacons_at_goal.add(bx)
    dist_to_goal = abs(goal - sy)
    absdx = abs(sx - bx)
    absdy = abs(sy - by)
    width = absdx - (dist_to_goal - absdy)
    if width < 0:
        continue
    adding = list(range(sx - width, sx + width + 1))
    beacons_missing.update(adding)

for b in beacons_at_goal:
    beacons_missing.discard(b)

print(len(beacons_missing))

# Part 2
def dist(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

scanners = {(a,b) : dist((a,b),(c,d)) for (a,b,c,d) in d}
left, right = set(), set()
for ((x,y), r) in scanners.items():
    left.add(y - x + r + 1)
    left.add(y - x - r - 1)
    right.add(y + x + r + 1)
    right.add(y + x - r - 1)

bounds = 4000000
def find_missing():
    for l in left:
        for r in right:
            p = ((r-l)//2, (r+l)//2)
            if all(0 < c < bounds for c in p) and all(dist(p,t) > scanners[t] for t in scanners.keys()):
                return p[0], p[1]

point = find_missing()
print(point[0] * 4000000 + point[1])