n = input()
n = n.split()
p = []
for i in range (len(n)):
    r = n[i][::-1]
    p.append(r)
print(*p)
