n = input()
n = n.split()
p = []
for i in range (len(n)):
    if i%2==0:
        r = n[i][::-1]
        p.append(r)
    else:
        p.append(n[i])
print(*p)
