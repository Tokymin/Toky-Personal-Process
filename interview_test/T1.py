# def min_length_after_join(n, m, block1, block2):
#     min_length = n + m  # 初始化为不拼接的长度之和
#
#     for i in range(-m + 1, n):  # 遍历所有可能的拼接位置
#         valid = True
#         length = max(n, m + i) - min(0, i)
#         for j in range(max(0, i), min(n, m + i)):
#             if int(block1[j]) + int(block2[j - i]) > 3:
#                 valid = False
#                 break
#         if valid:
#             min_length = min(min_length, length)
#
#     return min_length
#
# # 示例用法
# n, m = 3, 2
# block1 = "222"
# block2 = "22"
#
# result = min_length_after_join(n, m, block1, block2)
# print(result)


# def count_paths(n, m, a, roads):
#     dp = [[0] * (a + 1) for _ in range(n + 1)]
#     dp[1][0] = 1  # 从城市1出发，花费为0时的路径数为1
#
#     for ui, vi, wi in roads:
#         for j in range(a - wi + 1):
#             dp[vi][j + wi] += dp[ui][j]
#
#     result = dp[n][a]
#
#     # 如果路径数大于 20220201，则按照题目要求输出
#     if result > 20220201:
#         print("All roads lead to Home!")
#         print(result % 20220201)
#     else:
#         print(result)
#
#
# # 示例用法
# n = 3
# m = 6
# a = 2
# roads = [
#     (1, 2, 1),
#     (1, 2, 1),
#     (1, 2, 1),
#     (2, 3, 1),
#     (2, 3, 1),
#     (2, 3, 1)
# ]
#
# count_paths(n, m, a, roads)

# def min_length_after_join(n, m, block1, block2):
#     min_length = n + m  # 初始化为不拼接的长度之和
#
#     for i in range(-m + 1, n):  # 遍历所有可能的拼接位置
#         valid = True
#         length = max(n, m + i) - min(0, i)
#
#         # 使用滑动窗口检查每个位置的高度是否符合要求
#         for j in range(max(0, i), min(n, m + i)):
#             if int(block1[j]) + int(block2[j - i]) > 3:
#                 valid = False
#                 break
#
#         if valid:
#             min_length = min(min_length, length)
#
#     return min_length
#
#
# # 示例用法
# n, m = 3, 2
# block1 = "222"
# block2 = "22"
#
# result = min_length_after_join(n, m, block1, block2)
# print(result)

# def count_paths(n, m, a, roads):
#     # 初始化动态规划表
#     dp = [0] * (a + 1)
#     dp[0] = 1  # 从城市1出发，花费为0时的路径数为1
#
#     # 创建图
#     graph = [[] for _ in range(n + 1)]
#     for u, v, w in roads:
#         graph[u].append((v, w))
#
#     # 从城市1开始计算
#     for city in range(1, n + 1):
#         for cost in range(a, -1, -1):
#             if dp[cost] > 0:
#                 for vi, wi in graph[city]:
#                     new_cost = cost + wi
#                     if new_cost <= a:
#                         dp[new_cost] += dp[cost]
#                         dp[new_cost] %= 20220201  # 模运算
#
#     return dp[a]
#
#     # 输出结果
#     if result >= 20220201:
#         print("All roads lead to Home!")
#         print(result % 20220201)
#     else:
#         print(result)

MOD = 20220201

def get_path(n, a, roads):
    # n, m, a = map(int, input().split())
    dp = [[0] * (a + 1) for _ in range(n + 1)]
    dp[1][0] = 1

    # for _ in range(m):
    #     u, v, w = map(int, input().split())
    for u, v, w in roads:
        for j in range(a - w + 1):
            if dp[u][j]:
                dp[v][j + w] += dp[u][j]
                dp[v][j + w] %= MOD

    total_ways = sum(dp[n]) % MOD
    if total_ways >= 20220201:
        print("All roads lead to Home!")
    else:
        print(total_ways)

if __name__ == "__main__":
    # 测试用例1
    n = 3
    m = 6
    a = 2
    roads = [
        (1, 2, 1),
        (1, 2, 1),
        (1, 2, 1),
        (2, 3, 1),
        (2, 3, 1),
        (2, 3, 1)
    ]
    main(n, a, roads)
# count_paths(n, m, a, roads)  # 输出应为 9

    # 测试用例2：无效路径
    n = 3
    m = 3
    a = 3
    roads = [
        (1, 2, 1),
        (2, 3, 2),
        (1, 3, 4)
    ]
    main(n, a, roads)  # 输出应为 1 (路径：1->2->3)
#
# # 测试用例3：只有直接路径
# n = 2
# m = 1
# a = 5
# roads = [
#     (1, 2, 5)
# ]
# count_paths(n, m, a, roads)  # 输出应为 1 (路径：1->2)
#
    # 测试用例4：多个路径不同花费
    n = 4
    m = 5
    a = 4
    roads = [
        (1, 2, 2),
        (2, 3, 2),
        (1, 3, 3),
        (3, 4, 1),
        (2, 4, 2)
    ]
    main(n, a, roads)  # 输出应为 2 (路径：1->2->3->4, 1->3->4)

