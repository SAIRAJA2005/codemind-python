def fun(n):
    l = len(str(n))
    x = n 
    count=0
    while(n!=0):
        t = n%10
        if t==0:
            count=count
        elif (x%t==0):
            count+=1
        n=n//10
    if count==l:
        return 1
    else:
        return 0
m = int(input())
n = int(input())
for i in range(m,n+1):
    if fun(i)==1:
        print(i,end=" ")