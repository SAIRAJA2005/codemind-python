n = 3
n = int(input())
print(n,end = " ")
while(n>1 and n!=0):
    if n%2==0:
        n = n//2
        print(n,end = " ")
    else:
        n = n*3+1
        print(n,end = " ")