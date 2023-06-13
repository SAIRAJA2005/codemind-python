n = int(input())
r = list(map(int,input().split()))
l = []
for i in range(n//2,n):
    l.append(r[i])
l.reverse()
for i in range(0,n//2):
    l.append(r[i])
print(*l)