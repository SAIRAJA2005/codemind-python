n = input()
n = n.split()
c = 0
for i in range(len(n)):
    s = n[i]
    s = s.lower()
    s1 = s
    k = s[::-1]
    if (s1==k):
        c+=1
print(c)