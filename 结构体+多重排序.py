import sys

def solve():
    # 读取所有输入行
    lines=sys.stdin.read().split()
    # 读取第一个数字 n
    n=int(lines[0])
    students=[]
    index=1
    for i in range(n):
        c=int(lines[index])
        m=int(lines[index+1])
        e=int(lines[index+2])
        index += 3
        total=c+m+e
        sid = i + 1
        # 存储数据：为了方便排序，我们存储 (-总分, -语文, 学号)
        # 使用负数是因为 Python 默认排序是从小到大，
        # 负数越小代表原数值越大，从而实现“从高到低”排序
        students.append((-total,-c,sid))
    # 排序
    # Python 会自动先比较第一个元素，相同则比较第二个，以此类推
    students.sort()
    for i in range(5):
        # 取出排序后的数据
        neg_total,neg_chinese,s_id = students[i] 
        # 输出 学号 和 总分,把负数变回正数
        print(f"{s_id} {-neg_total}")
if __name__ == "__main__":
    solve()
