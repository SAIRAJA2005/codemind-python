n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    k  = sorted(l)
    print(k[-2])