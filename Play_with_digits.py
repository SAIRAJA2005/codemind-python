n = int(input())
l = list(map(int,input().split()))
s = 0
for i in l:
    x = i
    while(x!=0):
        r = x%10
        s+=r
        x=x//10
print(s)