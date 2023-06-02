a = int(input())
b = int(input())
for i in range (a,b):
    c=0
    for j in range(1,b):
        if i%j==0:
            c+=1
    if c==2:
        print(i)