import sys

# 设置递归深度，虽然本题用迭代法不需要，但作为DP题的习惯
sys.setrecursionlimit(200000)

def solve():
    # 读取输入
    try:
        line1 = sys.stdin.readline()
        n = int(line1.strip())
        s = sys.stdin.readline().strip()
        # 读取价值数组，注意题目中 a_i 对应长度 i，为了方便我们让 a[1] 对应长度 1
        a = list(map(int, sys.stdin.readline().split()))
    except ValueError:
        return
    # dp[i] 表示前 i 个字符的最大价值
    # 初始化为0，因为价值都是正整数，0 是最小下界
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        # 用于记录字符是否出现过
        seen = set()
        # 临时最大值，初始化为负无穷，但在本题逻辑中会被覆盖
        max_val = 0
        # 从当前位置 i-1 向前遍历，寻找合法的子串起点 j
        # 只需要遍历最多 26 个字符，或者直到字符串开头
        j = i - 1
        while j >= 0:
            char = s[j]
            # 如果遇到重复字符，停止向前查找
            if char in seen:
                break
            # 标记字符已出现
            seen.add(char)
            # 当前子串长度
            length = i - j
            # 当前子串的价值 + 剩余部分的最大价值
            # 注意 a 数组是 0-indexed，长度 length 对应 a[length-1]
            current_val = dp[j] + a[length - 1]
            if current_val > max_val:
                max_val = current_val
            j -= 1
        dp[i] = max_val
    print(dp[n])

if __name__ == "__main__":
    solve()
