def loader():
    stacks = [[] for _ in range(9)]
    for row in d[:8]:
        for i in range(1,len(row),4):
            if row[i] != " ":
                stacks[(i-1)//4].insert(0,row[i])
    return stacks

def solution(p):
    stacks = loader()

    if p:
        for _,v,_,a,_,b in [row.split(" ") for row in d[10:]]:
            stacks[int(b)-1] += stacks[int(a)-1][-int(v):]
            stacks[int(a)-1] = stacks[int(a)-1][:-int(v)]
    else:
        for _,v,_,a,_,b in [row.split(" ") for row in d[10:]]:
            for _ in range(int(v)):
                source = stacks[int(a)-1].pop()
                stacks[int(b)-1].append(source)

    return "".join([s[-1] for s in stacks])

d = open("5").read().split("\n")

print(solution(0))
print(solution(1))