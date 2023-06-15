n = int(input())
for i in range(n):
    k = int(input())
    l = list(map(int,input().split()))
    l1 = sorted(l)
    if l1 == l:
        print("0")
    else:
        print(max(l)-min(l))