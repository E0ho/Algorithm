# 두개의 재료 고유 번호 합 == M이면 갑옷

# 입력
N = int(input())
M = int(input())

li = list(map(int,input().split()))
li.sort()

# 투 포인트 지정
start_point = 0
end_point = len(li) - 1
count = 0
sum = li[start_point] + li[end_point]

while True:
    # 종료 조건
    if start_point == end_point:
        break
    
    # sum == M 인 경우
    if sum == M:
        count += 1
        sum -= li[start_point]
        start_point += 1
        sum += li[start_point]


    # 합이 M보다 큰 경우
    elif sum > M:
        sum -= li[end_point]
        end_point -= 1
        sum += li[end_point]


    # 합이 M보다 작은 경우
    else:
        sum -= li[start_point]
        start_point += 1
        sum += li[start_point]

print(count)