n = int(input())
l = list(map(int,input().split()))
x = int(input())
for i in l:
    if x in l:
        print (True)
        break
    else:
        print(False)
        break