

def build_line(start, end, blocks):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    steps = max(abs(dx), abs(dy)) + 1
    if start[0] == end[0]:
        # Vertical line
        blocks.update( (start[0], min(start[1],end[1]) + y) for y in range(steps) )
    elif start[1] == end[1]:
        # Horizontal line
        blocks.update( (min(start[0],end[0]) + x, start[1]) for x in range(steps) )

def simulate_step(sand, blocks):
    x = sand[0]
    y = sand[1]
    if (x, y + 1) not in blocks:
        return (x, y + 1)
    if (x - 1, y + 1) not in blocks:
        return (x - 1, y + 1)
    if (x + 1, y + 1) not in blocks:
        return (x + 1, y + 1)
    return sand # No change possible

def simulate(sand_spawn, blocks, depth_bound):
    sand = sand_spawn   
    while True:
        sand_next = simulate_step(sand, blocks)
        if sand_next == sand:
            return sand_next # Sand particle landed
        if part == 1 and sand_next[1] == depth_bound:
            return sand_next # Sand particle out of bounds
        sand = sand_next

def solution():
    d = [[(int(px),int(py)) for px, py in [point.split(",") for point in row.split(" -> ")]] for row in open("14").read().split("\n")]
    # Build blocks and find depth bound
    blocks = set()
    depth_bound = 0
    resting_sand_count = 0
    for row in d:
        start = row[0]
        blocks.add(start)
        for point in row[1:]:
            end = point
            depth_bound = max([start[1], end[1], depth_bound])
            build_line(start, end, blocks)
            start = end

    if part == 2:
        # Add floor
        blocks.update( (x, depth_bound + 2) for x in range(500 - (depth_bound+4), 500 + (depth_bound+4)) )

    while True:
        sand = simulate((500,0), blocks, depth_bound)     
        if part == 1 and sand[1] == depth_bound:
            # Sand is falling out of bounds, stop simulating
            break
        if part == 2 and sand[1] == 0:
            # Sand particle didnt leave spawn, stop simulating
            resting_sand_count += 1
            break
        resting_sand_count += 1
        blocks.add(sand) # Add this sand particle to permanent blocks

    return resting_sand_count

part = 1
print(solution())
part = 2
print(solution())