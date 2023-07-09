n = int(input())
k = 1
k2 = 1
c = 0
c1 = 0
for i in range(1,n+1):
    if (i%2!=0):
        print(k,end = " ")
        c = c+1
        k = 2**c
    else:
        print(k2,end = " ")
        c1 = c1 + 1
        k2 = 3**c1
        