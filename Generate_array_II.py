n = int(input())
l = list(map(int,input().split()))
b = []
for i in range(0,n,2):
    s = l[i]
    s1 = l[i+1]
    for i in range(1,s1+1):
        b.append(s)
print(*b)