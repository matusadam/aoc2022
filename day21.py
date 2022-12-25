import random

d = {name:val for name, val in [row.split(": ") for row in open("21").read().split("\n")]}

def ev(name):
    val = d[name].split(" ")
    if len(val) == 1:
        return int(val[0])
    else:
        n1, op, n2 = val
        match op:
            case "+": return ev(n1) +  ev(n2)
            case "-": return ev(n1) -  ev(n2)
            case "*": return ev(n1) *  ev(n2)
            case "/": return ev(n1) / ev(n2)

def ev2(name):
    left, _, right = d[name].split(" ")
    left_val = ev(left)
    right_val = ev(right)
    return left_val == right_val, left_val, right_val, abs(left_val-right_val), d["humn"]

# Part 1
print(ev("root"))

# Part 2
# TODO not generic solution
results = []
i = 1
while i < 100000:
    rnum = random.randint(3848301405818-230,3848301405818+230,)
    if not i % 1000:
        print(f"checked {i} numbers")
    d["humn"] = str(rnum)
    r = ev2("root")
    results.append(r)
    if r[0]:
        print(rnum)
        break  
    i+=1

results = sorted(results, key=lambda r: r[3])
for res in results[:50]:
    print(res)

