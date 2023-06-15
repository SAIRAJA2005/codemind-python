n = int(input())
for i in range(n):
    a,b=map(int,input().split())
    if a>b:
        print("LOSS")
    elif a==b:
        print("NEUTRAL")
    else:
        print("PROFIT")