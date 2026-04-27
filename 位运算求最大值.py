import sys

def solve():
    # 使用 sys.stdin.readline 提高输入效率
    input = sys.stdin.readline
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
        a = list(map(int, input().split()))
    except ValueError:
        return
    max0=0
    # 从高位（30位）向低位（0位）进行贪心检查
    for i in range(30, -1, -1):
        # 尝试将当前位设为 1
        c = max0 | (1 << i)
        # 统计数组中有多少个数满足条件
        count = 0
        for num in a:
            # 检查 num 是否包含 candidate 的所有 1 位
            if (num & c) == c:
                count += 1
        # 如果至少有两个数满足条件，说明这一位可以是 1
        if count >= 2:
            max0 = c
    print(max0)

if __name__ == "__main__":
    solve()
