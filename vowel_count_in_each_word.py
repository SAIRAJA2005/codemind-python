n = input()
n = n.split()
for i in range(len(n)):
    c = 0
    r = n[i]
    k = "aeiouAEIOU"
    for i in range(len(r)):
        if r[i] in k:
            c+=1
    print(c,end=" ")