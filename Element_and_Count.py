n = int(input())
l = list(map(int,input().split()))
a = []
c = []
for i in l:
    if i not in a:
        a.append(i)
        b = l.count(i)
        c.append(b)
for i in range(len(a)):
    print(a[i],c[i],end=" ")