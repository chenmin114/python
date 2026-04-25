import sys

def solve():
    # 读取第一行 M 和 N
    # 使用 sys.stdin 读取以处理可能的输入缓冲问题
    input_line = sys.stdin.readline().strip()
    M, N = map(int, input_line.split())
    products = []
    for _ in range(N):
        line = sys.stdin.readline().strip().split()
        name = line[0]
        price = int(line[1])
        priority = int(line[2])
        products.append({
            'name': name,
            'price': price,
            'priority': priority,
            'bought': False
        })
    budget = M
    bought_items = []  
    while True:
        # 1. 筛选出当前预算能买得起且未购买的商品
        candidates = [p for p in products if not p['bought'] and p['price'] <= budget]        
        # 2. 如果没有候选商品，结束循环
        if not candidates:
            break         
        # 3. 找到最优商品
        # Python 的元组比较会自动按照顺序比较元素
        # 我们需要：优先级V最小 -> 价格P最小 -> 名字字典序最小
        # 所以 key 直接取 (priority, price, name) 即可
        best_product = min(candidates, key=lambda x: (x['priority'], x['price'], x['name']))       
        # 4. 更新状态
        best_product['bought'] = True
        budget -= best_product['price']
        bought_items.append(best_product['name'])       
    # 5. 按字典序排序并输出
    bought_items.sort()
    for name in bought_items:
        print(name)
if __name__ == "__main__":
    solve()
