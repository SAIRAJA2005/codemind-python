m,n=map(int,input().split())
r = list(map(int,input().split()))
r1 = list(map(int,input().split()))
t = []
for i in r:
    if i in r1:
        if i not in t:
            t.append(i)
for i in r1:
    if i in r:
        if i not in t:
            t.append(i)
print(*t)