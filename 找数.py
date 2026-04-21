# 读取输入
n,m=map(int,input().split())
A=set(map(int,input().split()))
B=set(map(int,input().split()))
# 计算交集并输出结果
common_elements=A.intersection(B)
print(len(common_elements))
