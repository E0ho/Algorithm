# 입력
t, w = tuple(map(int, input().split()))

# DP[초][이동 횟수] -> (2진 트리)
dp = [
    [0] * (t + 2)           # 0 패딩
    for _ in range(t + 1)   # 0 패딩
]

# 자두 나무
tree = [0]
for _ in range(t):
    tree.append(int(input()))   # 자두 받기

# print('tree :', tree)


# 자두 줍기 시작
for second in range(1, len(tree)):
    
    # 현재 초에 해당하는 이동 경우의 수
    for move_count in range(1, second + 2):
        
        # 현재 2번 나무이며, 2번 나무가 떨어진다면 +1
        if move_count % 2 == 0 and tree[second] == 2:
            dp[second][move_count] = max(dp[second-1][move_count], dp[second-1][move_count-1]) + 1

        # 현재 1번 나무이며, 1번 나무가 떨어진다면 +1
        elif move_count % 2 == 1 and tree[second] == 1:
            dp[second][move_count] = max(dp[second-1][move_count], dp[second-1][move_count-1]) + 1

        else:
            dp[second][move_count] = max(dp[second-1][move_count], dp[second-1][move_count-1])


# print('DP')

max_num = 0
for line in dp:
    line = line[:w + 2]        # 최대 이동 횟수 제한
    max_num = max(max(line), max_num)

print(max_num)
