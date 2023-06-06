n = input()
v = "aeiou"
r = []
for i in range(len(n)):
    if n[i] in v:
        if n[i] not in r:
            r.append(n[i])
if len(v)==len(r):
    print("0")
else:
    for i in v:
        if i not in r:
            print(i,end=" ")
    
    