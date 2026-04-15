import random
import time

class BonusPoolGame:
    def __init__(self):
        # 初始化奖池数据（根据图片内容）
        # 100元 x 1
        # 50元 x 2
        # 20元 x 3
        # 10元 x 10
        # 炸弹 x 8
        self.pool = ( [100] * 1 +  [50] * 2 + [20] * 3 + [10] * 10 + [0] * 8 )
        self.max_attempts = 10      # 总共十次机会
        self.target_amount = 100    # 提现目标
        self.current_balance = 0    # 当前累计奖金
        self.attempts = 0           # 当前抽取次数
    def play(self):
        print("游戏开始！")
        print(f"规则：总共 {self.max_attempts} 次机会，累计满 {self.target_amount} 元可提现。")
        print(f"注意：抽到炸弹游戏结束且奖金清零！")
        print("-" * 30)
        # 游戏主循环
        while self.attempts < self.max_attempts:
            self.attempts += 1
            print(f"\n第 {self.attempts} 次抽取...", end="")
            time.sleep(0.8) # 模拟抽取的等待时间，增加紧张感
            # 随机抽取
            prize = random.choice(self.pool)
            # 判定逻辑
            if prize == 0:
                print(f" 抽到了 [{prize}]！！！")
                print("boom! 游戏结束，之前的奖金全部清零！")
                self.current_balance = 0
                break
            else:
                # 抽到奖金
                self.current_balance += prize
                # 从奖池中移除该奖金（不放回抽取）
                self.pool.remove(prize)
                print(f" 抽到了 [{prize}元]，当前累计：{self.current_balance}元")
                # 检查是否达成提现条件
                if self.current_balance >= self.target_amount:
                    print(f"恭喜！累计金额达到 {self.current_balance}元，成功提现！")
                    break
        # 游戏结束总结
        print("-" * 30)
        if self.current_balance > 0 and self.current_balance < self.target_amount and self.attempts >= self.max_attempts:
            print("机会用尽，游戏结束。")
            print(f"最终结果：遗憾，未达成提现目标，最终持有 {self.current_balance}元（虚拟币）。")
        elif self.current_balance >= self.target_amount:
             print("游戏胜利！")
        else:
            print("游戏失败！")

if __name__ == "__main__":
    game = BonusPoolGame()
    game.play()
