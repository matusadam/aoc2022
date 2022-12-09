import math
from itertools import chain

d = [r.split(" ") for r in open("9").read().split("\n")]

def solution(knot_count):
    moves = chain(*[[{"R":(1,0),"U":(0,-1),"L":(-1,0),"D":(0,1)}[m]] * int(c) for m,c in d])
    knots = [[0,0] for _ in range(knot_count)]
    visited = {}
    visited_counter = 0
    for move in moves:
        knots[0][0] += move[0]
        knots[0][1] += move[1]
        for i in range(knot_count-1):
            head = knots[i]
            tail = knots[i+1]
            dx = tail[0] - head[0]
            dy = tail[1] - head[1]
            move_ff = lambda x: (lambda y: math.ceil(y/2) if y>0 else math.floor(y/2))(x) if abs(dx) > 1 or abs(dy) > 1 else 0
            tail[0] -= move_ff(dx)
            tail[1] -= move_ff(dy)
            if i == knot_count-2 and tuple(tail) not in visited:
                visited[tuple(tail)] = None
                visited_counter += 1
    return visited_counter

print(solution(2))
print(solution(10))