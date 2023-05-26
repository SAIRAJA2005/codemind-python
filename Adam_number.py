x = int(input())
w = x
x1 = x * x

s = str(w)
s1 = len(s)
s2 = s[s1::-1]

a = int(s2)
a1 = a*a

z = str(a1)
z1 = len(z)
z2 = z[z1::-1]
z3 = int(z2)

if x1 == z3:
    print("True")
else:
    print("False")