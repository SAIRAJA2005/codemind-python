n = int(input())
x = list(map(int,input().split()))
s = 0
d = 0
for i in range (n):
    if  i%2==0:
        s = s + x[i]
    if  i%2!=0:
        d = d + x[i]
print(abs(s-d))