n = int(input())
l = list(map(int,input().split()))
a = []
c = 0
for i in l:
    if i==l.count(i):
        if i not in a:
            a.append(i)
            c = 1
if c==1:
    p = sum(a)/len(a)
    print(format(p,".2f"))
else:
    print("-1")