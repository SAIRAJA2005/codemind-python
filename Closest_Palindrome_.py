def fun(n):
    r = n
    t = 0
    while (r!=0):
        y = r%10
        t = t*10+y
        r = r//10
    if t==n:
        return 1
    else:
        return 0
        
n = int(input())
for i in range (n+1,2 * n):
    if fun (i) == 1:
        s = i
        break
    
for i in range (n-1,0,-1):
    if fun (i) == 1:
        a = i
        break 
    
if abs(s-n) == abs(a-n):
    print(a,s)
elif abs(s-n) < abs(a-n):
    print(s)
else:
    print(a)
    