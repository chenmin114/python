import sys

# 设置递归深度，虽然归并排序通常不需要太深，但防止极端情况
sys.setrecursionlimit(20000)
def solve():
    # 读取输入
    try:
        # 读取所有输入并按空格分割
        input_data = sys.stdin.read().split()
        iterator = iter(input_data)
        n = int(next(iterator))   
        students = []
        for _ in range(n):
            h = int(next(iterator))
            w = int(next(iterator))
            students.append((h, w))         
    except StopIteration:
        return
    # 归并排序计算逆序对
    # temp 数组用于归并过程中的临时存储
    temp = [0] * n
    count = 0
    def merge_sort(left, right):
        nonlocal count
        if left >= right:
            return
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        # 合并过程
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            # 判断 students[i] 是否应该排在 students[j] 前面
            # 规则：身高降序，身高相同则体重降序
            # 即：(h1 > h2) or (h1 == h2 and w1 > w2)
            h1, w1 = students[i]
            h2, w2 = students[j]
            should_come_before = False
            if h1 > h2:
                should_come_before = True
            elif h1 == h2 and w1 > w2:
                should_come_before = True
            if should_come_before:
                temp[k] = students[i]
                i += 1
            else:
                # 如果 students[j] 应该排在 students[i] 前面
                # 说明 students[i] 到 students[mid] 的所有元素相对于 students[j] 都是逆序的
                temp[k] = students[j]
                count += (mid - i + 1)
                j += 1
            k += 1
        # 处理剩余元素
        while i <= mid:
            temp[k] = students[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = students[j]
            j += 1
            k += 1   
        # 将排序好的部分复制回原数组
        for i in range(left, right + 1):
            students[i] = temp[i]
    # 执行排序
    merge_sort(0, n - 1)
    # 输出结果
    print(count)

if __name__ == "__main__":
    solve()
