import sys
def solve():
    # 读取第一行 n 和 k
    # 使用 sys.stdin.readline 读取速度更快，也可以直接用 input()
    try:
        line = sys.stdin.readline()
        n, k = map(int, line.split())
    except ValueError:
        return
    boxes = []
    # 循环读取每个礼盒的数据
    for i in range(n):
        line = sys.stdin.readline()           
        prices = list(map(int, line.split()))       
        # 计算统计值
        total_price = sum(prices)
        max_price = max(prices)
        min_price = min(prices)   
        # 保存信息：(总价, 最大值, 最小值, 原始编号)
        # 编号从 1 开始，所以是 i + 1
        boxes.append((total_price, max_price, min_price, i + 1))
    # 排序
    # Python 的元组排序会自动按照第一个元素比较，相同则比较第二个，以此类推
    # 这完美契合题目要求的 4 个优先级顺序
    boxes.sort()
    # 输出结果
    # 提取排序后的编号
    result_ids = [str(box[3]) for box in boxes]
    # 使用空格连接并打印
    print(" ".join(result_ids))

if __name__ == "__main__":
    solve()
