import re
from functools import cache

d = [re.findall(r"\d+", row) for row in open("19").read().split("\n")]

def parse_blueprint(bp):
    return int(bp[0]),int(bp[1]),int(bp[2]),int(bp[3]),int(bp[4]),int(bp[5]),int(bp[6])


def simulate(m1,m2,m3,m4,r1,r2,r3,r4,t):

    rs = list()

    # Plan ore robot purchase
    # Dont need more ore robots than what is needed to satisfy ore requirement of any of the robots in one timestep
    if r1 < ore_maxneeded:
        need = (bp[1] - m1)
        td = (0 if need <= 0 else 1 + (need-1) // r1) + 1
        if t+td <= TIMELIMIT:
            rs.append( 
                simulate( m1-bp[1]+r1*td, m2 + r2*td, m3 + r3*td, m4 + r4*td, r1+1, r2, r3, r4, t+td) 
            )
    
    # Plan clay robot purchase
    # Dont need more clay robots than what is needed to build obsidian robot in one timestep
    if r2 < bp[4]:
        need = (bp[2] - m1)
        td = (0 if need <= 0 else 1 + (need-1) // r1) + 1
        if t+td <= TIMELIMIT:
            rs.append( 
                simulate( m1 - bp[2] + r1*td, m2 + r2*td, m3 + r3*td, m4 + r4*td, r1, r2+1, r3, r4, t+td) 
            )

    # Plan obsidian robot purchase
    # Need at least one clay robot to consider this branch, 
    # and also dont need more obsidian robots than what is needed to build geode robot in one timestep
    if r2 > 0 and r3 < bp[6]: 
        need_ore = (bp[3] - m1)
        need_clay = (bp[4] - m2)
        td_ore = (0 if need_ore <= 0 else 1 + (need_ore-1) // r1) + 1
        td_clay = (0 if need_clay <= 0 else 1 + (need_clay-1) // r2) + 1
        td = max(td_clay, td_ore)
        if t+td <= TIMELIMIT:
            rs.append( 
                simulate( m1 - bp[3] + r1*td, m2 - bp[4] + r2*td, m3 + r3*td, m4 + r4*td, r1, r2, r3+1, r4, t+td) 
            )

    # Plan geode robot purchase
    # Need at least one obsidian robot to consider this branch
    if r3 > 0: 
        need_ore = (bp[5] - m1)
        need_obsidian = (bp[6] - m3)
        td_ore = (0 if need_ore <= 0 else 1 + (need_ore-1) // r1) + 1
        td_obsidian = (0 if need_obsidian <= 0 else 1 + (need_obsidian-1) // r3) + 1
        td = max(td_obsidian, td_ore)
        if t+td <= TIMELIMIT:
            rs.append( 
                simulate( m1 - bp[5] + r1*td, m2 + r2*td, m3 - bp[6] + r3*td, m4 + r4*td, r1, r2, r3, r4+1, t+td) 
            )

    if not rs: # No plan exists from this time until the TIMELIMIT
        return (TIMELIMIT+1-t) * r4 + m4
    else:
        return max(rs)


TIMELIMIT = 24
summ = 0
for raw_bp in d:
    bp = parse_blueprint(raw_bp)
    ore_maxneeded = max([bp[1], bp[2], bp[3], bp[5]])
    ret = simulate( 0,0,0,0, 1,0,0,0, 1)
    print(ret)
    summ += ret * bp[0]
print(summ)

TIMELIMIT = 32
prod = 1
for raw_bp in d[:3]:
    bp = parse_blueprint(raw_bp)
    ore_maxneeded = max([bp[1], bp[2], bp[3], bp[5]])
    ret = simulate( 0,0,0,0, 1,0,0,0, 1)
    print(ret)
    prod *= ret
print(prod)