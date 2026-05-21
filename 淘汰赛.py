def solve():
    try:
        line1 = input().strip()
        n = int(line1)
        powers = list(map(int, input().strip().split()))
    except EOFError:
        return
    # 初始化队伍列表，存储 (编号, 能力值)
    # 编号从 1 开始，对应 powers 的索引 0
    teams = [(i + 1, powers[i]) for i in range(len(powers))]
    # 模拟淘汰赛过程
    # 只要队伍数量大于 2，就继续比赛
    while len(teams) > 2:
        next_round = []
        # 两两配对比赛
        # 每次步进 2，取出 teams[i] 和 teams[i+1]
        for i in range(0, len(teams), 2):
            team1 = teams[i]
            team2 = teams[i + 1]
            # 能力值高的晋级
            if team1[1] > team2[1]:
                next_round.append(team1)
            else:
                next_round.append(team2)
        # 更新队伍列表为下一轮的晋级者
        teams = next_round
    # 此时 teams 中只剩下 2 个队伍，即决赛双方
    # 比较能力值，能力值较小的为亚军
    finalist1 = teams[0]
    finalist2 = teams[1]
    if finalist1[1] < finalist2[1]:
        print(finalist1[0])
    else:
        print(finalist2[0])

if __name__ == "__main__":
    solve()
