def selfd(n):
    l=len(str(n))
    cnt=0
    r=n
    while n!=0:
        t=n%10
        if(t==0):
            cnt=cnt
        elif r%t==0:
            cnt+=1
        n=n//10
    if cnt==l:
        return 1
    else:
        return 0
m = int(input())
n = int(input())
for i in range(m,n+1):
    if selfd(i)==1:
        print(i,end=" ")