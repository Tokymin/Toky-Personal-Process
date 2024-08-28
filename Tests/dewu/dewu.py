def T2():
    def longest_valid_prefix_length(s):
        stack = []
        max_length = 0
        current_length = 0

        for c in s:
            if c == '(':
                stack.append(c)
                current_length += 1
            elif c == ')' and stack:
                stack.pop()
                current_length += 1
            max_length = max(max_length, current_length)

        return max_length

    # 输入
    n = int(input())
    s = input()

    # 输出
    result = longest_valid_prefix_length(s)
    print(result)

def T1():
    from itertools import combinations
    def calc_probability(n, k, a):
        # 计算每个人完全获胜的概率
        win_probs = []
        for i in range(n):
            prob = 1.0
            for j in range(n):
                if i != j:
                    prob *= a[i] / (a[i] + a[j])
            win_probs.append(prob)
        total_prob = 0.0

        # 考虑选择 k 个人获胜的所有组合
        for winners in combinations(range(n), k):
            prob = 1.0
            for i in range(n):
                if i in winners:
                    prob *= win_probs[i]  # 选中的人必须全部获胜
                else:
                    prob *= (1 - win_probs[i])  # 未选中的人必须全部失败
            total_prob += prob
        return total_prob

    # 输入
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # 计算并输出结果
    result = calc_probability(n, k, a)
    print(f"{result:.2f}")


def T3():
    def min_cost_to_transform(t, p, q):
        n = len(t)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # 从空字符串开始

        for i in range(1, n + 1):
            # 操作1和操作2: 在前后添加一个字符
            dp[i] = dp[i - 1] + p

            # 操作3和操作4: 在前后添加子串
            for j in range(i):
                if t[j:i] in t[:j]:
                    dp[i] = min(dp[i], dp[j] + q)

        return dp[n]

    # 输入
    t = input().strip()
    p, q = map(int, input().split())

    # 输出
    result = min_cost_to_transform(t, p, q)
    print(result)


if __name__ == '__main__':
    T2()