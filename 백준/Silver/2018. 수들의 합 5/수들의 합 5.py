# N -> 연속된 수의 합으로 표현할 수 있는 개수
# 정렬 -> 투포인터로 구간 좁히기

# 입력
N = int(input())

start_value = 1
end_value = 1
count = 1
sum = 1

# 연속된 수의 합
while True:

    # 종료 조건
    if end_value == N:
        break
        
    # 투 포인터 이동 조건
    # 동일한 경우 count 증가, (종료 + 1) 더하기
    if sum == N:
        count += 1
        end_value += 1
        sum += end_value

    # 작은 경우 -> (종료 + 1) 더하기
    elif sum < N:
        end_value += 1
        sum += end_value

    # 큰 경우 -> 시작 뺴기
    else:
        sum -= start_value
        start_value += 1


print(count)