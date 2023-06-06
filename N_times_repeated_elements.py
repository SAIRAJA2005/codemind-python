k = int(input())
l = list(map(int,input().split()))
r = int(input())
a = []
c = 0
for i in l:
    if l.count(i)==r:
        if i not in a:
            c = 1
            a.append(i)
if c==0:
    print("-1")
else:
    print(*a)
    