import sys

def solve():
    # 提高递归限制（虽然下面使用了迭代法，但保留此习惯以防万一）
    sys.setrecursionlimit(300000)
    # 使用 sys.stdin.readline 读取输入，速度更快
    input = sys.stdin.readline
    # 1. 读取 n
    line = input().strip()
    while line == '':
        line = input().strip()
    n = int(line)
    # 2. 构建树结构
    children = [[] for _ in range(n + 1)]
    if n > 1:
        # 读取父节点行
        parents_line = input().strip()
        while parents_line == '':
            parents_line = input().strip()
        parents = list(map(int, parents_line.split()))  
        # 根据题目：第 i 个数表示编号 (i+1) 的节点的父节点
        for i in range(n - 1):
            p = parents[i]
            child_id = i + 2
            children[p].append(child_id)
    # 3. 读取初始颜色
    colors_line = input().strip()
    while colors_line == '':
        colors_line = input().strip()
    # 转为列表方便修改，'1'表示黑，'0'表示白
    res = list(colors_line)
    # 4. 读取操作次数 q
    q_line = input().strip()
    while q_line == '':
        q_line = input().strip()
    q = int(q_line)
    # 5. 统计每个节点被直接操作的次数（差分数组思想）
    ops = [0] * (n + 1)
    for _ in range(q):
        op_line = input().strip()
        while op_line == '':
            op_line = input().strip()
        node = int(op_line)
        ops[node] += 1
    # 6. 使用迭代 DFS 计算最终颜色
    # 栈中存储 (当前节点, 当前累积翻转次数)
    # 初始时根节点1的累积翻转次数为 ops[1]
    stack = [(1, ops[1])]
    while stack:
        node, curr_flips = stack.pop()
        # 判断当前节点颜色是否需要翻转
        # 如果累积翻转次数是奇数，颜色改变；偶数则不变
        if curr_flips % 2 == 1:
            if res[node - 1] == '1':
                res[node - 1] = '0'
            else:
                res[node - 1] = '1'
        # 将子节点压入栈
        # 子节点的累积翻转次数 = 父节点的累积翻转次数 + 子节点自身的直接操作次数
        for child in children[node]:
            stack.append((child, curr_flips + ops[child]))
    # 输出结果
    print(''.join(res))

if __name__ == '__main__':
    solve()
