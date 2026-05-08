import sys

def solve():
    # 使用 sys.stdin.readline 读取输入以提高效率
    input=sys.stdin.readline
    # 读取 N (关卡数) 和 M (通道数)
    line=input().split()
    n, m=map(int, line)
    # 读取 M 个通道的前进距离
    a=list(map(int, input().split()))
    # 读取 N 个关卡的分数
    b=list(map(int, input().split()))
    # dp[i] 表示从第 i 关出发能获得的最大分数
    # 初始化为 0
    dp=[0]*n
    # 从最后一关开始，倒序向前计算
    for i in range(n-1,-1,-1):
        max_future_score=float('-inf')
        # 遍历所有通道，找到能获得最大未来分数的路径
        for jump in a:
            next_pos=i+jump
            # 如果下一位置超出或等于 N，说明直接通关，未来分数为 0
            if next_pos>=n:
                future_score=0
            else:
                # 否则，未来分数就是从下一位置开始的最大分数
                future_score=dp[next_pos]
            # 更新当前能获得的最大未来分数
            max_future_score=max(max_future_score,future_score)
        # 当前关卡的最大总分 = 当前关卡分数 + 最大未来分数
        dp[i]=b[i]+max_future_score
    # 最终答案是第 0 关的最大分数
    print(dp[0])
if __name__=="__main__":
    solve()
