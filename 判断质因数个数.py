n=int(input())
for _ in range(n):
    num=int(input())
    count=0
    t=num
    if t%2==0:
        count+=1
        while t%2==0:
            t=t//2
    i=3
    while i*i<=t:
        if t%i==0:
            count+=1
            while t%i==0:
                t=t//i
        i+=2        
    if t>2:
        count+=1
    if count==2:
        print("1")
    else:
        print("0")
