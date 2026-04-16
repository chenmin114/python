import sys
import bisect

def solve():
    # 1. 快速读取所有输入数据
    # sys.stdin.buffer.read() 读取字节流，速度最快
    input_data = sys.stdin.buffer.read().split()
    
    if not input_data:
        return

    # 2. 解析 n 和 m
    # 使用迭代器来遍历数据，比用下标访问更快且优雅
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    # 3. 读取数组 a
    a = []
    for _ in range(n):
        a.append(int(next(it)))
    
    # 4. 处理查询
    res = []
    for _ in range(m):
        q = int(next(it))
        # 使用 bisect_left 找到第一个 >= q 的位置
        idx = bisect.bisect_left(a, q)
        
        # 检查该位置是否真的等于 q（防止查找到比 q 大的数，或者越界）
        if idx < n and a[idx] == q:
            # 题目要求编号从 1 开始，所以 +1
            res.append(str(idx + 1))
        else:
            res.append(str(-1))
            
    # 5. 一次性输出结果
    sys.stdout.write(' '.join(res))

if __name__ == '__main__':
    solve()
