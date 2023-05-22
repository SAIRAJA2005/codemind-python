n = int(input())
a = 0
b = 1
c = a+b
cnt = 0
l = []
while(cnt<1000):
    #print(a,end=' ')
    l.append(a)
    a = b
    b = c
    c = a+b
    cnt+=1
if n in l:
    print(True)
else:
    print(False)
