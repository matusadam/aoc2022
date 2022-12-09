
def check2(i,j,tree):

    # Left
    left = 0
    for t in reversed(d[i][:j]):
        left += 1
        if int(t) >= tree:
            break
    # Right
    right = 0
    for t in d[i][j+1:]:
        right += 1
        if int(t) >= tree:
            break
    # Top
    top = 0
    for t in reversed([int(r[j]) for r in d[:i]]):
        top += 1
        if t >= tree:
            break
    # Bottom
    bottom = 0
    for t in [int(r[j]) for r in d[i+1:]]:
        bottom += 1
        if t >= tree:
            break
    ret = left*right*bottom*top
    return ret

def check(i,j,tree):
    
    try:
        # Left
        if tree > max([int(t) for t in d[i][:j]]):
            return 1
        # Right
        if tree > max([int(t) for t in d[i][j+1:]]):
            return 1
        # Top
        if tree > max([int(r[j]) for r in d[:i]]):
            return 1
        # Bottom
        if tree > max([int(r[j]) for r in d[i+1:]]):
            return 1
    except ValueError:
        return 1
    return 0
    
d = open("8").read().split("\n")

summ = 0
for i,row in enumerate(d):
    for j,tree in enumerate(row):
        summ += check(i,j,int(tree))
print(summ)

maximum = 0
for i,row in enumerate(d):
    for j,tree in enumerate(row):
        v = check2(i,j,int(tree))
        if v > maximum:
            maximum = v
print(maximum)