n = int(input())
l = list(map(int,input().split()))
q,w = map(int,input().split())
a = []
c = 0
for i in range(n):
    if l[i]>=q and l[i]<=w:
        continue
    else:
        c=1
        a.append(l[i])
if (c==0):
    print("-1")
else:
    print(*a)