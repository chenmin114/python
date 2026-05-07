import sys

def solve():
    # 读取第一行 N 和 L
    line=sys.stdin.readline()
    n,L= map(int,line.split())
    drinks=[]
    for _ in range(n):
        c,l=map(int, sys.stdin.readline().split())
        drinks.append((c,l))
    # 定义无穷大
    INF = float('inf')
    # dp[j] 表示凑出至少 j 容量所需的最小花费
    # 数组大小只需要 L + 1，因为超过 L 的容量我们都视为 L
    dp=[INF]*(L+1)
    # 初始状态：凑出 0 容量花费为 0
    dp[0]=0
    # 遍历每种饮料
    for c, l in drinks:
        # 0/1 背包必须倒序遍历容量，防止同一物品被重复选取
        # 我们从 L 遍历到 0
        for j in range(L,-1,-1):
            if dp[j]!=INF:
                # 计算购买当前饮料后的新容量
                # 如果超过 L，直接截断为 L
                new= min(L,j+l)
                # 更新状态：取“不买”和“买”之间的最小值
                if dp[new]>dp[j]+c:
                    dp[new]=dp[j]+c
    # 输出结果
    if dp[L] == INF:
        print("no solution")
    else:
        print(dp[L])

if __name__ == "__main__":
    solve()
