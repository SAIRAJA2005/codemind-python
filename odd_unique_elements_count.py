k = int(input())
l = list(map(int,input().split()))
a=[]
for i in l:
    if i%2!=0:
        if i not in a:
            a.append(i)
print(len(a))
    