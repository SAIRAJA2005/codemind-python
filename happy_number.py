n=int(input())
while(n//10!=0):
    x=0; 
    while(n!=0):
        rem=n%10 
        x=x+rem*rem 
        n=n//10 
    n=x
if(x==1 or x==7):
    print(True) 
else:
    print(False)