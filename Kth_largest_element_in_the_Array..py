n = int(input())
l = list(set(map(int,input().split())))
k = int(input())
m = sorted(l)
f = m[len(l)-k]
print(f)
