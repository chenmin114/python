import sys

def solve():
    # 读取输入
    input_line = sys.stdin.readline().strip()
    n, b = map(int, input_line.split())
    # 初始化数组，记录每个数的最大质因子
    # 0 表示尚未处理（或者是质数本身）
    max_prime_factors = [0] * (n + 1)
    # 线性筛/埃氏筛变种
    for i in range(2, n + 1):
        # 如果 max_prime_factors[i] 为 0，说明 i 是质数
        if max_prime_factors[i] == 0:
            # i 是质数，它的最大质因子就是它自己
            max_prime_factors[i] = i       
            # 更新 i 的所有倍数的最大质因子
            # 从 2*i 开始，步长为 i
            for j in range(i * 2, n + 1, i):
                # 因为我们是从小到大遍历 i，所以后面遇到的质因子一定比前面的大
                # 直接覆盖即可
                max_prime_factors[j] = i       
    # 统计数量
    # 1 是 B-smooth 数（因为它没有质因子 > B）
    count=1     
    for i in range(2,n + 1):
        if max_prime_factors[i] <= b:
            count += 1   
    print(count)

if __name__ == "__main__":
    solve()
