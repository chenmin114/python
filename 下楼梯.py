import sys

n=int(input())
if n==1:
    print(1)
elif n==2:
    print(2)
elif n==3:
    print(4)
else:
    f1=1
    f2=2
    f3=4
    for i in range(4,n+1):
        x=f1+f2+f3
        f1=f2
        f2=f3
        f3=x
    print(x)
    
