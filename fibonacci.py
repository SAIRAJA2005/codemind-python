n = int(input())
a = 0
b = 1
c = a+b
cnt = 0
while(cnt<n):
    print(a,end=' ')
    a = b
    b = c
    c = a+b
    cnt+=1
