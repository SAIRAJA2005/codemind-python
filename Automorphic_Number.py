n = int(input())
n1 = len(str(n))
k = n*n
if (n == k%10**n1):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")