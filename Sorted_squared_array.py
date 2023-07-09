n = int(input())
l = list(map(int,input().split()))
p = []
for i in l :
    c = i*i
    p.append(c)
p.sort()
print(*p)