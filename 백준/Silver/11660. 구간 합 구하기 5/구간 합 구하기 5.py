# 구간 합 문제
# 합 배열

# 다중 입력 옵션
import sys
input = sys.stdin.readline

# 입력
N, M = tuple(map(int, input().split()))
li = [[0] * (N + 1)]

for _ in range(N):
    row = [0] + list(map(int, input().split()))
    li.append(row)
   

# 합 배열
s = [[0] * (N + 1) for _ in range(N + 1)]


# 합 배열 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        s[i][j] = (s[i-1][j] + s[i][j-1]) - s[i-1][j-1] + li[i][j]

# 구간 합
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] + s[x1 - 1][y1 - 1] - (s[x1 - 1][y2] + s[x2][y1 - 1]))