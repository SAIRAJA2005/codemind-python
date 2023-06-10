n = int(input())
for i in range(n):
    k = int(input())
    r = list(map(int,input().split()))
    r1 = r
    if r1==sorted(r):
        print("0")
    else:
        r.sort()
        t = min(r)
        t1 = max(r)
        print(abs(t-t1))