n = int(input())
while n > 9:
    d = 0 
    while n > 0:
        r = n % 10 
        d += r 
        n //= 10
    n = d
print(n)