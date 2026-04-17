import sys
import math

def solve():
    # 读取点的数量 N
    line=sys.stdin.readline()
    if not line:  return
    n=int(line.strip()) 
    points = []   
    # 读取 N 个点的坐标
    for _ in range(n):
        x,y,z=map(int,sys.stdin.readline().split())
        # 将点存入列表，为了方便排序，我们存为 (z,x,y) 的形式
        points.append((z,x,y))  
    # 1. 排序
    # 题目要求从最低点爬到最高点，即按照 z 从小到大排序
    # Python 的 sort 默认会按照元组的第一个元素（这里是 z）排序
    points.sort()
    # 2. 计算总距离
    sum=0.0 
    for i in range(n-1):
        z1,x1,y1=points[i]
        z2,x2,y2=points[i+1]     
        s=math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)        
        sum+=s 
    # 3. 输出结果，保留三位小数
    print(f"{sum:.3f}")
if __name__ == "__main__":
    solve()
