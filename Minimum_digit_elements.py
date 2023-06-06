n = int(input())
l = list(map(int,input().split()))
t = min(l)
t1= len(str(t))
p = []
for i in l:
    r = len(str(i))
    if t1==r:
        p.append(i)
print(len(p))
        
        
        
        