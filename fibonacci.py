n = int(input())
count=0
x=0
y=1
while(count<n):
    print(x,end=' ')
    d = x + y
    x = y
    y = d
    count+=1