n = input()
v = "aeiouAEIOU"
f = 0
for i in n:
    if i in v:
        f+=1
print(f)