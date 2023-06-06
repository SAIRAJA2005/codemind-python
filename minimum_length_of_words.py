n = input()
n = n.split()
p = []
for i in n:
    p.append(len(i))
print(min(p))