d = [(int(a[0]),int(a[1]),int(b[0]),int(b[1]))for a,b in[[y.split("-")for y in x.split(",")]for x in open("4").read().split("\n")]]
print(sum(1 if k>=m and l<=n or m>=k and n<=l else 0 for k,l,m,n in d))
print(sum(0 if l<m or n<k else 1 for k,l,m,n in d))