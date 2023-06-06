n = int(input())
l = list(map(int,input().split()))
c  = 0
for i in range(n):
    if l[i]!=0 and l[i]!=1:
        c = 1
    else:
        continue
if(c==1):
    print(False)
else:
    print(True)