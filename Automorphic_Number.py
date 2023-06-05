n = int(input()) 
r = n 
t = n*n 
e = len(str(r)) 
a = 10**e
if t%a==r:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")