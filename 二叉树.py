import sys
# 设置递归深度，防止树退化为链状时递归溢出
sys.setrecursionlimit(200005)

def solve():
    # 读取节点数 n
    # 使用 sys.stdin.readline 加速输入
    input=sys.stdin.readline
    n_line=input().strip()
    if not n_line:
        return
    n=int(n_line)
    # 初始化子节点列表
    children=[[] for _ in range(n + 1)]
    # 读取父节点信息构建树 (如果 n > 1)
    if n>1:
        parents_input=list(map(int,input().split()))
        # 输入的第 i 个数是节点 (i+1) 的父节点
        for i in range(n-1):
            p = parents_input[i]
            children[p].append(i + 2)
    # 读取初始颜色字符串
    # 注意：题目输入的是字符串，例如 '100101'
    s = input().strip()
    # 将字符转换为整数列表，方便计算 (0或1)
    # index 0 对应节点 1
    init_colors=[int(c) for c in s]
    # 读取操作次数 q
    q=int(input().strip())
    # diff 数组记录每个节点被“直接操作”的次数
    diff=[0]*(n + 1)
    # 读取 q 次操作
    for _ in range(q):
        u=int(input().strip())
        diff[u]+=1   
    # 结果列表
    res = []
    def dfs(u, current_flips):
        # 计算当前节点的总翻转次数
        # 当前节点被翻转的总次数 = 祖先传递下来的翻转次数 + 自己作为根被操作的次数
        total_flips=current_flips+diff[u]   
        # 获取初始颜色 (节点 u 对应列表索引 u-1)
        initial_color=init_colors[u-1] 
        # 如果翻转次数是奇数，颜色改变；偶数则不变
        # 使用异或运算 ^ 1 实现翻转
        if total_flips%2==1:
            final_color=initial_color^1
        else:
            final_color=initial_color 
        res.append(str(final_color))
        # 递归处理子节点，将当前的总翻转次数传递下去
        for v in children[u]:
            dfs(v,total_flips)
    # 从根节点 1 开始，初始累积翻转次数为 0
    dfs(1,0)
    # 输出结果
    print(''.join(res))

if __name__=='__main__':
    solve()
