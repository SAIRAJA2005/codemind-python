def fun(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n = int(input())
l = list(map(int,input().split()))
d = 1
f = 1
for i in l:
    if fun(i)==1:
        f = f*i
    if fun(i)==0:
        d = d*i
print(abs(f-d))
        