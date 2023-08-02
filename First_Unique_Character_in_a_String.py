n = input()
l = list(n)
k = len(l)
a = []
for i in range(k):
    if l.count(l[i])==1:
        print(i)
        break
else:
    print('-1')