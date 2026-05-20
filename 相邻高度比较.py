import sys
line1=sys.stdin.readline().strip()
n,m=map(int,line1.split())
a=[]
for _ in range(n):
    row=list(map(int,sys.stdin.readline().strip().split()))
    a.append(row)
d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
ans=0
for i in range(n):
    for j in range(m):
        h=a[i][j]
        flag=True
        for di,dj in d:
            ni,nj=i+di,j+dj
            if 0<=ni<n and 0<=nj<m:
                if a[ni][nj]<h:
                    flag=False
                    break
        if flag:
            ans+=1
print(ans)            
