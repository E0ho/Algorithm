# 입력
n = int(input())
scores = list(map(int, input().split()))

# 점수 조작
maxi = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i] / maxi * 100

# 출력 (점수 평균)
print(sum(scores) / len(scores))