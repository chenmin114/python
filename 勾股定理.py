import math
n=int(input())
ans=0
for a in range(1,n+1):
    for b in range(a,n+1):
        c2=a*a+b*b
        if c2>n*n:
            break
        c=int(math.sqrt(c2))
        if c*c==c2:
            ans+=1
print(ans)                
