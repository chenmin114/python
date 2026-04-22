import sys

def solve():
    input_data=sys.stdin.read().split()
    iterator=iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return
    students = [] 
    # 1. 读取数据并预处理关键指标
    for i in range(n):
        c = int(next(iterator))
        m = int(next(iterator))
        e = int(next(iterator))   
        total = c + m + e
        cm_sum = c + m
        cm_max = max(c,m)    
        # 存储：(原始索引, 总分, 语数总分, 语数最高分)
        students.append({
            'idx': i,
            'total': total,
            'cm_sum': cm_sum,
            'cm_max': cm_max
        })
    # 2. 自定义排序
    # Python的sort是稳定的，且元组比较是从左到右依次比较
    # 使用负数实现降序排序
    students.sort(key=lambda x: (-x['total'], -x['cm_sum'], -x['cm_max']))
    # 3. 计算排名
    ranks = [0] * n
    for i in range(n):
        if i == 0:
            ranks[students[i]['idx']]=1
        else:
            prev=students[i-1]
            curr=students[i]      
            # 检查三项指标是否完全相同
            if (curr['total'] == prev['total'] and 
                curr['cm_sum'] == prev['cm_sum'] and 
                curr['cm_max'] == prev['cm_max']):
                # 如果相同，排名与前一名一样
                ranks[curr['idx']] = ranks[prev['idx']]
            else:
                # 如果不同，排名为当前位置 + 1 (实现了并列后跳名的逻辑)
                ranks[curr['idx']] = i + 1          
    for r in ranks:
        print(r)
if __name__ == "__main__":
    solve()
