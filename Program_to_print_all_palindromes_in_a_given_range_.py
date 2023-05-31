a=int(input())
b=int(input())
for i in range (a,b):
    f = i
    re=0
    while(i>0):
        d = i%10
        re = re*10+d
        i = i//10
    if (f==re):
        print(re,end=' ')
    else:
        continue