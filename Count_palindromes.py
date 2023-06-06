n = int(input())
l = list(map(int,input().split()))
p = 0
for i in l:
    x = i
    s = 0
    while(x!=0):
        r = x%10
        s = s*10+r
        x=x//10
    if i==s:
        p+=1
print(p)
        