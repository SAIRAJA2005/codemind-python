n = int(input())
k = list(map(int,input().split()))
a = []
for i in k:
    if i not in a:
        a.append(i)
print(*a)