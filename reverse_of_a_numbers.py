n=int(input())
x=0
while(n!=0):
    rem=n%10
    x=(x*10)+rem
    n=n//10
print(x)