import sys
# 增加递归深度限制，防止树退化成链导致递归溢出
sys.setrecursionlimit(300000)

def solve():
    # 读取节点数量
    try:
        line=sys.stdin.readline()
        n=int(line.strip())
    except ValueError:
        return
    # 构建邻接表
    adj=[[] for _ in range(n+1)]
    for _ in range(n-1):
        u,v=map(int,sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    # color数组用于存储每个节点的颜色（0或1），-1表示未访问
    color=[-1]*(n+1)
    # count数组用于统计每种颜色的节点数量
    count=[0,0]
    def dfs(u,c):
        color[u]=c
        count[c]+=1
        for v in adj[u]:
            if color[v]==-1:
                # 相邻节点染成相反的颜色 (1-c)
                dfs(v,1-c)
    # 从节点1开始染色，初始颜色为0
    dfs(1,0)
    # 输出结果
    res=[]
    for i in range(1,n+1):
        # 节点i能到达的偶数步节点数 = 与节点i颜色相同的节点总数
        res.append(str(count[color[i]]))
    print(" ".join(res))

if __name__=="__main__":
    solve()
