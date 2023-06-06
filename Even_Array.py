n = int(input())
k = list(map(int,input().split()))
p = len(k)
c = 0
for i in k:
    if i%2==0:
        c+=1
if c==p:
    print(True)
else:
    print(False)