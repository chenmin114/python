import sys

def solve():
    n=int(sys.stdin.readline())
    a=list(map(int, sys.stdin.readline().split()))
    b=list(map(int, sys.stdin.readline().split()))
    # 为了方便，我们将数组下标从1开始处理
    # a[0] 对应题目中的 a1, b[0] 对应题目中的 b1
    # 我们虚拟一个下标0，a[-1] = 0, b[-1] = 1 (但这里我们用列表索引0来表示下标1)
    # dp[i] 表示以第 i 个元素 (1-based) 结尾的最大和
    dp=[0]*(n+1)
    # events[i] 存储在位置 i 解锁的所有 dp[j] 值
    # 即，对于某个 j，如果 j + b[j] == i，那么 dp[j] 会被加入到 events[i] 中
    events=[[] for _ in range(n + 2)] # +2 防止越界
    # 虚拟下标0，dp[0] = 0，它能到达位置 0 + 1 = 1
    # 所以在位置1，我们有一个候选值0
    events[1].append(0)
    max_val=0 # 当前能到达位置 i 的所有 dp[j] 中的最大值
    for i in range(1,n+1):
        # 更新 max_val：将所有在位置 i 解锁的 dp[j] 值考虑进来
        for val in events[i]:
            if val>max_val:
                max_val=val   
        # 计算 dp[i]
        # a[i-1] 是第 i 个元素的值 (因为 a 是 0-based)
        dp[i]=a[i-1]+max_val
        # 将 dp[i] 作为一个新的候选者，它将在位置 i + b[i-1] 解锁
        next_pos=i+b[i-1]
        if next_pos<=n:
            events[next_pos].append(dp[i])
        # 如果 next_pos > n，说明这个选择无法再跳到后面，无需记录
    # 答案是所有 dp[i] 中的最大值
    print(max(dp[1:]))

solve()
