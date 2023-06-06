n = int(input())
l = list(map(int,input().split()))
e = 0
s = 0
for i in range(n-1,-1,-1):
    e = e+l[i]*(2**s)
    s+=1
print(e)