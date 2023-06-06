n = input()
n1 = input()
v = "aeiou"
r = []
for i in range(len(n)):
    if n[i] in v:
        if n[i]==n1:
            print(True)
            print(i)
            break
else:
    print(False)

    
    