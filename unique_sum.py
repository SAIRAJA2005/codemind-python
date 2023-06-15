n = int(input())
l = list(map(int,input().split()))
a = []
c = 0
for i in l:
    if i not in a:
        a.append(i)
s = 0
for i in a:
    s+=i
print(s)