import sys
sys.setrecursionlimit(5000)

from functools import cache

@cache
def wrap(x,y,z):
    if (x,y,z) in exterior:
        return # Already added
    exterior.add( (x,y,z) )
    flip = sides[x,y,z]
    if (x % 2) == 0: # YZ plane
        for fy in [1, -1]: # Pos and neg Y
            if (x+flip, y+fy, z) in sides: wrap(x+flip, y+fy, z)
            elif (x, y+fy*2, z) in sides: wrap(x, y+fy*2, z)
            else: wrap(x-flip, y+fy, z)

        for fz in [1, -1]: # Pos and neg Z
            if (x+flip, y, z+fz) in sides: wrap(x+flip, y, z+fz)
            elif (x, y, z+fz*2) in sides: wrap(x, y, z+fz*2)
            else: wrap(x-flip, y, z+fz)

    if (y % 2) == 0: # XZ plane
        for fx in [1, -1]: # Pos and neg X
            if (x+fx, y+flip, z) in sides: wrap(x+fx, y+flip, z)
            elif (x+fx*2, y, z) in sides: wrap(x+fx*2, y, z)
            else: wrap(x+fx, y-flip, z)

        for fz in [1, -1]: # Pos and neg Z
            if (x, y+flip, z+fz) in sides: wrap(x, y+flip, z+fz)
            elif (x, y, z+fz*2) in sides: wrap(x, y, z+fz*2)
            else: wrap(x, y-flip, z+fz)

    if (z % 2) == 0: # XY plane
        for fx in [1, -1]: # Pos and neg X
            if (x+fx, y, z+flip) in sides: wrap(x+fx, y, z+flip)
            elif (x+fx*2, y, z) in sides: wrap(x+fx*2, y, z)
            else: wrap(x+fx, y, z-flip)

        for fy in [1, -1]: # Pos and neg Y
            if (x, y+fy, z+flip) in sides: wrap(x, y+fy, z+flip)
            elif (x, y+fy*2, z) in sides: wrap(x, y+fy*2, z)
            else: wrap(x, y+fy, z-flip)

d = [(int(x)*2,int(y)*2,int(z)*2) for x,y,z in [c.split(",") for c in open("18").read().split("\n")]]

sides = dict()
for x,y,z in d:

    if (x+1,y+1,z) not in sides: sides[x+1,y+1,z] = -1
    else: del sides[x+1,y+1,z]

    if (x+1,y,z+1) not in sides: sides[x+1,y,z+1] = -1
    else: del sides[x+1,y,z+1]

    if (x,y+1,z+1) not in sides: sides[x,y+1,z+1] = -1
    else: del sides[x,y+1,z+1]

    if (x+2,y+1,z+1) not in sides: sides[x+2,y+1,z+1] = 1
    else: del sides[x+2,y+1,z+1]

    if (x+1,y+2,z+1) not in sides: sides[x+1,y+2,z+1] = 1
    else: del sides[x+1,y+2,z+1]

    if (x+1,y+1,z+2) not in sides: sides[x+1,y+1,z+2] = 1
    else: del sides[x+1,y+1,z+2]

# Part 1  
print(len(sides))

max_x = 0
max_x_side = None
for x,y,z in sides:
    if x > max_x:
        max_x = x
        max_x_side = (x,y,z)

exterior = set()
x,y,z = max_x_side

wrap(x,y,z)

# Part 2
print(len(exterior))