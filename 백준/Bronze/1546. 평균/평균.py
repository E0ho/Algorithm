# 최고점 구하기
# 변경된 값 저장하기

# 입력
n = int(input())
li = list(map(int, input().split()))
new_li = []

# 최고점 구하기
max_score = max(li)

# 변경된 값 저장
for score in li:
    new_li.append(score / max_score * 100)

# 새로운 평균 출력
print(sum(new_li) / len(new_li))