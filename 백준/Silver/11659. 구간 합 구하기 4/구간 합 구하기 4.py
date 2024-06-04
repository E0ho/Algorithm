# 구간 합 문제
# 합 배열을 통해 Timeout 방지

# 다중 입력 설정
import sys
input = sys.stdin.readline

# 입력
N, M = tuple(map(int, input().split()))
li = list(map(int, input().split()))

s = [0]
temp = 0

# 합 배열 구하기
for ele in li:
    temp += ele
    s.append(temp)
    
# 구간 합
for _ in range(M):
    i, j = map(int, input().split())
    print(s[j] - s[i-1])