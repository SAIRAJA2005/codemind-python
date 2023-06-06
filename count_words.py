n = input()
n = n.split()
v = 'AEIOUaeiou'
cnt = 0
for i in range(len(n)):
    r = n[i]
    if r[0] in v and r[-1] not in v:
        cnt+=1
print(cnt)
    
    