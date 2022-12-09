d = open("6").read()
# Part 1
print([i for i in range(4, len(d)) if len(set(d[i-4:i])) == 4])
# Part 2
print([i for i in range(14, len(d)) if len(set(d[i-14:i])) == 14])