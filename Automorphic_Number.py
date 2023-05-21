n=int(input())
string=str(n)
square=n**2
if (n==square%(10**len(string))):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")