def solve():
    try:
        # 读取输入的正整数 n
        n = int(input())
        # 初始化当前字符的索引，0 对应 'A'
        current_char_index=0
        # 外层循环：控制行数，从 1 到 n
        for i in range(1,n+1):
            line_content = ""
            # 内层循环：控制每一行打印 i 个字符
            for j in range(i):
                # 计算当前字符：chr(ord('A') + 0) = 'A', ..., chr(ord('A') + 25) = 'Z'
                char_to_print=chr(ord('A')+(current_char_index%26))
                # 拼接到当前行字符串
                line_content+=char_to_print
                # 字符索引递增，准备下一个字符
                current_char_index+=1
            # 打印当前行
            print(line_content)
    except ValueError:
        pass
if __name__ == "__main__":
    solve()
