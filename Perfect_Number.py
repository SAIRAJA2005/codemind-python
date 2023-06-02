
n = int(input())
x = n
s = 0
for i in range(1,n):
    if (n%i==0):
        s+=i
if (s==x):
    print(True)
else:
    print(False)
