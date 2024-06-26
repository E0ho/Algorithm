# 배열의 왼쪽으로 붙여 이동 방향을 아래 / 아래 오른쪽으로 변경
# 합이 최대 -> DP
# dx, dy
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
def solution(triangle):
    answer = 0
    n = len(triangle)
    
    dp = [[0] * (n + 1)
         for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i-1][j-1]
            
    answer = (max(dp[-1]))
    
    return answer



#     n = len(triangle)
    
#     # dp (0 패딩 적용)
#     dp = [[0] * (n + 1)]
#     for _ in range(n):
#         dp.append([0] * (n + 1))
    
#     # 더 큰 값으로 더하기 (그래프를 좌측으로 붙여 위, 왼쪽 위)
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i-1][j-1]
    
#     # 최종 출력 층 최대 값
#     answer = max(dp[n])