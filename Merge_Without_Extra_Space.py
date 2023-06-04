n = int(input())
for i in range (0,n):
    s,k=map(int,input().split())
    r=list(map(int,input().split()))
    p=list(map(int,input().split()))
    u = r+p
    k = sorted(u)
    print(*k)