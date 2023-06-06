n = int(input())
k = list(map(int,input().split()))
m = []
c = 0
for i in k:
    if i==k.count(i):
        if i not in m:
            m.append(i)
            c = 1
if c==1:
    print(*m)
else:
    print("-1")