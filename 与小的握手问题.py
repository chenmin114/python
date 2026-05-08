import sys

# 设置递归深度，防止在极端情况下（如N=300000）递归过深导致栈溢出
sys.setrecursionlimit(10**6)

def merge_sort_count(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2     
        # 递归统计左半边和右半边的顺序对
        count += merge_sort_count(arr, temp, left, mid)
        count += merge_sort_count(arr, temp, mid + 1, right)
        # 统计跨越左右两边的顺序对，并进行合并
        count += merge(arr, temp, left, mid, right) 
    return count

def merge(arr, temp, left, mid, right):
    i = left    # 左半部分指针
    j = mid + 1 # 右半部分指针
    k = left    # 临时数组指针
    count = 0
    # 合并过程
    while i <= mid and j <= right:
        # 如果左边的数 < 右边的数，满足题目握手条件
        if arr[i] < arr[j]:
            # 此时 arr[i] 比右边数组中从 j 到 right 的所有数都小
            # 贡献的顺序对数量为：(right - j + 1)
            count += (right - j + 1)
            temp[k] = arr[i]
            i += 1
        else:
            # 如果 arr[i] >= arr[j]，不满足握手条件，直接放入
            temp[k] = arr[j]
            j += 1
        k += 1 
    # 复制剩余元素
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    # 将排序好的部分复制回原数组
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return count

def solve():
    # 使用 sys.stdin.read 读取所有输入，比 input() 快得多
    input_data = sys.stdin.read().split()
    if not input_data:
        return     
    n = int(input_data[0])
    arr = list(map(int, input_data[1:]))
    temp = [0] * n
    result = merge_sort_count(arr, temp, 0, n - 1)
    print(result)

if __name__ == "__main__":
    solve()
