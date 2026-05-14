import sys
# 增加递归深度限制（虽然本题用迭代法不需要，但这是一个好习惯）
sys.setrecursionlimit(200000)

def solve():
    # 读取输入
    try:
        line1=sys.stdin.readline()
        n=int(line1.strip())
        line2=sys.stdin.readline()     
        # 读取积极度数组
        # a[i] 表示 i 个人的小组的积极度
        # 为了方便对应，我们在数组头部补一个 0，使得 a[1] 对应 1 个人的积极度
        a_vals=list(map(int,line2.strip().split()))
        a = [0]*(n+1)
        for i in range(1,n+1):
            a[i]=a_vals[i-1]
    except ValueError:
        return
    # 初始化 DP 数组
    # dp[i] 表示 i 个人时的最大积极度之和
    # 初始化为 0，因为积极度是非负的，0 是合法的下界
    dp=[0]*(n+1)
    # 开始动态规划
    # 外层循环：枚举总人数，从 1 到 n
    for i in range(1,n + 1):
        # 内层循环：枚举最后一个小组的人数 j
        # j 的范围是 1 到 i
        max_val=0
        for j in range(1,i+1):
            # 状态转移方程：
            # 当前 i 个人的最优解 = max(之前算出的最优解, 剩下 i-j 人的最优解 + 当前 j 人组的积极度)
            current_val=dp[i-j]+a[j]
            if current_val>max_val:
                max_val=current_val
        dp[i]=max_val
    # 输出结果
    print(dp[n])

if __name__ == "__main__":
    solve()
