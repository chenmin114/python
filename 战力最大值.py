import sys

def solve():
    # 提高输入读取速度
    input = sys.stdin.readline
    try:
        line1 = input().strip()
        n, k = map(int, line1.split())
    except ValueError:
        return
    items = []
    total_attack = 0
    for _ in range(n):
        a, c = map(int, input().split())
        items.append((a, c))
        total_attack += a
    # --- 核心优化算法 ---
    # 1. 使用整数作为 Bitset 来记录哪些攻击力是可达的
    # 初始状态：第0位为1，表示攻击力0是可达的
    bits = 1
    # cost[i] 将存储达到攻击力 i 所需的最小金币
    # 初始化为无穷大
    cost = [float('inf')] * (total_attack + 1)
    cost[0] = 0
    for a, c in items:
        # 计算新的可达攻击力状态
        # bits << a 表示所有已有的攻击力都加上了 a
        # | 运算表示取并集（原来的状态 + 新的状态）
        new_bits = bits | (bits << a)
        # 找出这一轮**新增**的攻击力位
        # 只有新增的位才需要更新 cost，因为我们要找最小花费
        added_bits = new_bits ^ bits
        if added_bits:
            # 将新增的位转换为二进制字符串并反转，方便通过索引找到是哪一位
            # 注意：bin() 返回 '0b...', 所以要去掉前缀
            b_str = bin(added_bits)[2:][::-1]
            # 遍历新增的位，更新对应的最小花费
            # 由于新增的位通常远少于总位数，这个循环非常快
            for j in range(len(b_str)):
                if b_str[j] == '1':
                    # 达到 j 点攻击力的花费 = 达到 (j-a) 点的花费 + 当前道具花费
                    cost[j] = cost[j - a] + c
            bits = new_bits
    # 从最大攻击力向下查找，找到第一个花费 <= k 的
    for ans in range(total_attack, -1, -1):
        if cost[ans] <= k:
            print(ans)
            return

if __name__ == "__main__":
    solve()
