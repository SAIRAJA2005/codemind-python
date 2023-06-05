x = int(input())
n = x
c = 0
while n!=0:
    r=n%10
    u = 1
    for i in range(r,0,-1):
        u = u*i
    c=c+u
    n = n//10
if x==c:
    print("The number",x,"is a strong number")
else:
    print("The number",x,"is not a strong number")
        