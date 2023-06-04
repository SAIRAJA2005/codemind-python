s = list(map(int,input().split()))
k = list(map(int,input().split()))
r=l=o=0
for i in range(len(s)):
    if s[i]>k[i]:
        r+=1
    elif s[i]<k[i]:
        l+=1
    else:
        o+=1
print(r,l)
        