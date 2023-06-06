n = input()
n = n.split()
r = []
for i in range(len(n)):
    r.append(n[i])
r.reverse()
print(*r)    
    
    