n = int(input())
l = list(map(int,input().split()))
b = []
for i in range(0,n,2):
    k = l[i]
    k1 = l[i+1]
    for i in range(1,k1+1):
        b.append(k)
print(*b)