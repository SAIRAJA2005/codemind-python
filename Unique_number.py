x=int(input())
n=str(x)
s=list(n)
q=set(n)
if len(s)==len(q): 
    print("Unique Number")
else:
    print("Not Unique Number")