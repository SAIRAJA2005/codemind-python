n = input()
g = list(n)
r = []
c = 0
k = "aeiouAEIOU"
for i in range(len(g)):
    if g[i] in k:
        if g[i] not in r:
            c = 1
            r.append(g[i])
if c==0:
    print("-1")
else:
    print(*r)