m,n=map(int,input().split())
l = list(map(int,input().split()))
r = []
for i in range(n,m):
    r.append(l[i])
for i in range(0,n):
    r.append(l[i])
print(*r)
