d = open("3").read().split('\n')
print(sum((ord((set(l[len(l)//2:])&set(l[:len(l)//2])).pop())-38)%58 for l in d))
print(sum((ord((set.intersection(*d[i:i+3])).pop())-38)%58 for i in range(0,len(d),3)))