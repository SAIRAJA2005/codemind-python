
import math
n = int(input())
for i in range(n):
    a = int(input())
    b = math.sqrt(a)
    if (int(b)**2==a):
        print(True)
    else:
        print(False)

