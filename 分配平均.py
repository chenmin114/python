import sys

def solve():
    # 读取所有输入数据
    input=sys.stdin.read
    data=input().split()
    # 解析输入
    iterator=iter(data)
    try:
        n=int(next(iterator))
    except StopIteration:
        return
    # 读取b数组
    b_list=[]
    for _ in range(2*n):
        b_list.append(int(next(iterator)))
    # 读取c数组
    c_list=[]
    for _ in range(2*n):
        c_list.append(int(next(iterator)))
    # 构建物品列表包含(差值,b价格,c价格)
    items=[]
    for i in range(2*n):
        diff=b_list[i]-c_list[i]
        items.append((diff,b_list[i],c_list[i]))
    # 按照差值从大到小排序
    # 差值越大，说明卖给B越划算
    items.sort(reverse=True,key=lambda x:x[0])
    max_income=0
    for i in range(n):
        max_income+=items[i][1] 
    for i in range(n,2*n):
        max_income+=items[i][2] 
    print(max_income)

if __name__ == "__main__":
    solve()
