
import re
from itertools import product
from functools import cache
from collections import defaultdict

d = [re.findall(r"[A-Z]{2}|\d+", row) for row in open("16").read().split("\n")]
valves = set()
flows = dict()
edges = defaultdict(lambda: 999999999)
for row in d:
    valve = row[0]
    flow = int(row[1])
    connections = row[2:]
    valves.add(valve)
    if flow != 0: 
        flows[valve] = flow
    for conn in connections: 
        edges[conn, valve] = 1

for k, i, j in product(valves, valves, valves):
    edges[i,j] = min(edges[i,j], edges[i,k] + edges[k,j])

@cache
def run(time_remaining, start, valves_remaining):
    best_flow = 0
    for next_valve in valves_remaining:
        if edges[start, next_valve] < time_remaining:
            fl = flows[next_valve] * (time_remaining - edges[start, next_valve]-1) \
                + run(time_remaining - edges[start, next_valve] - 1, next_valve, valves_remaining - {next_valve})
            best_flow = max(best_flow, fl)
    return best_flow

@cache
def run2(time_remaining, start, valves_remaining):
    best_flow = 0
    for next_valve in valves_remaining:
        if edges[start, next_valve] < time_remaining:
            fl = flows[next_valve] * (time_remaining - edges[start, next_valve]-1) \
                + run2(time_remaining - edges[start, next_valve] - 1, next_valve, valves_remaining - {next_valve})
            best_flow = max(best_flow, fl)
    # Pathing for elephant
    best_flow = max(best_flow, run(26, "AA", valves_remaining))
    return best_flow

print(run(30, "AA", frozenset(flows)))
print(run2(26, "AA", frozenset(flows)))