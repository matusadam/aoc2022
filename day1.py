print(max(sum(int(x) for x in d.split("\n")) for d in open("1").read().split("\n\n")))
print(sum(sorted([sum(int(x) for x in d.split("\n")) for d in open("1").read().split("\n\n")])[-3:]))