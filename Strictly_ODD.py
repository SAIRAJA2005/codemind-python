n = int(input())
l = list(map(int,input().split()))
p = 0
c = 0
for i in range(len(l)):
    if i%2!=0:
        p+=1
        if l[i]%2!=0:
            c+=1
if p==c:
    print(True)
else:
    print(False)