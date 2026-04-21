import sys
import math

def solve():
    input=sys.stdin.readline
    n,q=map(int,input().split())
    a=list(map(int, input().split()))
    # 计算差值 gcd
    g=0
    for j in range(1,n):
        g=math.gcd(g,abs(a[j]-a[0]))
    # 处理询问
    out_lines=[]
    for j in range(q):
        i=j+1
        ans=math.gcd(a[0]+i,g)
        out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))
if __name__=="__main__":
    solve()
