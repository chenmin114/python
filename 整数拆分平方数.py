import math

def num_squares(n):
    # 初始化 dp 数组
    # dp[i] 表示组成数字 i 所需的最少完全平方数个数
    # 初始化为 i，因为最坏的情况是 i 由 i 个 1 组成 (1^2 + 1^2 + ...)
    dp=[i for i in range(n+1)]
    # 从 1 开始计算每个数的最少数量
    for i in range(1,n+1):
        j=1
        # 遍历所有小于等于 i 的完全平方数
        while j*j<=i:
            # 状态转移方程：
            # 当前数 i 的最优解 = min(当前值, 减去一个完全平方数后的最优解 + 1)
            dp[i]=min(dp[i],dp[i-j * j]+1)
            j+=1  
    return dp[n]

if __name__=="__main__":
    try:
        # 读取一行整数
        n_str=input().strip()
        if n_str:
            n=int(n_str)
            # 计算并输出结果
            print(num_squares(n))
    except ValueError:
        print("请输入有效的整数")
