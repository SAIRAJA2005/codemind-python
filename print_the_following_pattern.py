n = int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print("",end=" ")
    for j in range(1,i+1):
        print(i,end="")
    for j in range(1,i):
        print(i,end="")
    print()