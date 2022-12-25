d = open("10").read().split("\n")

cycle = 1
acc = 1
history = [(1, 1)]

for ins in d:
    if ins == "noop":    
        history.append((cycle+1, acc))
        cycle+=1
    else:    
        history.append((cycle+1, acc))
        _, value = ins.split(" ")
        value = int(value)
        acc += value 
        history.append((cycle+2, acc))
        cycle+=2
     
history_p1 = history[19::40]
result = 0
for cycle, val in history_p1:
    result += cycle*val
print(result)


# Part 2
render = []
for cycle, val in history:
    pixel = (cycle - 1)%40
    if pixel - 1 == val or pixel == val or pixel + 1 == val:
        render.append("#")
    else:
        render.append("_")

result = ""
for i,c in enumerate(render):
    result += c
    result += " "
    if i%40 == 39:
        result += "\n"

print(result)