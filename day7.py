d = open("7").read().split("\n")

root = {
    "parent" : None,
    "size" : 0,
    "children" : {}
}

cwd = root

all_dirs = {'/': root}

path = []

for line in d:
    if line[:4] == "$ cd":
        name = line[5:]
        if name == "/":
            cwd = root
            path = []
        elif name == "..":
            cwd = cwd['parent']
            path.pop()
        else:
            cwd = cwd['children'][name]
            path.append(name)
    elif line[:4] == "$ ls":
        pass
    elif line[:3] == "dir":
        name = line[4:]
        if name not in cwd['children']:
            newdir = {"parent": cwd, "size": 0, "children":{}}
            cwd['children'][name] = newdir
            all_dirs["/" + "/".join(path) + f"{name}"] = newdir
    else:
        size, name = line.split(" ")
        if name not in cwd['children']:
            cwd['children'][name] = {"parent": cwd, "size": int(size), "children":None}
            buildup = cwd
            while buildup:
                buildup['size'] += int(size)
                buildup = buildup['parent']

result = 0
for dirname,dir in all_dirs.items():
    print(dirname, dir['size'])
    if dir['size'] <= 100000:
        result += dir['size']

print(result)

# Part 2
unused = 70000000 - all_dirs["/"]['size']
needed = 30000000 - unused
smallest = all_dirs["/"]['size']
for dirname,dir in all_dirs.items():
    if dir['size'] >= needed and dir['size'] < smallest:
        smallest = dir['size']
print(smallest)
