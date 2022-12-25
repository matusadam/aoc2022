from functools import cmp_to_key

def comp(left: list, right: list) -> int:
    for l, r in zip(left,right):
        match l,r:
            case int(), int(): ret = l - r
            case int(), list(): ret = comp([l],r)
            case list(), int(): ret = comp(l,[r])
            case list(), list(): ret = comp(l,r)
        if ret:
            return ret
    return len(left) - len(right)

packets = [eval(x) for x in open("13").read().split("\n") if len(x) > 0]

# Part 1
print(sum(i//2 + 1 for i in range(0, len(packets), 2) if comp(packets[i], packets[i+1]) < 0))

# Part 2
packets = sorted(packets + [[[2]],[[6]]], key=cmp_to_key(comp))
print((packets.index([[2]])+1) * (packets.index([[6]])+1))