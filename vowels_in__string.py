n = input()
g = list(n)
r = []
c = 0
k = ["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(g)):
    if g[i] in k:
        if g[i] not in r:
            c = 1
            r.append(g[i])
if c==0:
    print("-1")
else:
    for i in r:
        print(i,end=" ")
    
    