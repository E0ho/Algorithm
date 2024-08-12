import sys
input = sys.stdin.readline

# 입력
n, m = tuple(map(int, input().split()))
li = list(map(int, input().split()))

# 합 배열
s = [0]
for ele in li:
    s.append(ele + s[-1])

# 구간 합
for _ in range(m):
    i, j = map(int, input().split())
    
    # 출력
    print(s[j] - s[i - 1])