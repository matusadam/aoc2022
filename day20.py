
def mix(d):
    for index_to_move in range(dl):
        for i in range(dl):
            if d[i][0] == index_to_move:
                nd = list()
                offset = d[i][1]
                newpos = i
                while offset:
                    newpos = newpos + offset
                    offset = newpos // dl  # Count the loops of this move
                    newpos = newpos % dl
                # print(f"i {i} val {d[i][1]} off {offset}, newpos {newpos}")
                if newpos > i:
                    nd = d[:i] + d[i+1:newpos+1] + [d[i]] + d[newpos+1:]
                elif newpos < i:
                    nd = d[:newpos] + [d[i]] + d[newpos:i] + d[i+1:]
                else:
                    nd = d
                d = nd
                break
    print([x[1] for x in d])
    return d


# Part 1
d = [[i,int(x)] for i,x in enumerate(open("20").read().split("\n"))]
dl = len(d)
d = mix(d)

for i,e in enumerate(d):
    if e[1] == 0:
        print(sum(d[(i+step)%dl][1] for step in [1000,2000,3000]))


# Part 2
d = [[i,811589153*int(x)] for i,x in enumerate(open("20").read().split("\n"))]
dl = len(d)
print([x[1] for x in d])
for _ in range(10):
    d = mix(d)

for i,e in enumerate(d):
    if e[1] == 0:
        print(sum(d[(i+step)%dl][1] for step in [1000,2000,3000]))
