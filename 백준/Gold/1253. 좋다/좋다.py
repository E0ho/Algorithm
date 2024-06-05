# 좋은 수 -> 다른 두 수으로 표현되는 수
# 투 포인터 전략

# 입력
N = int(input())
li = list(map(int, input().split()))

# 정렬
li.sort()
count = 0

# 리스트 내 원소 하나씩 검사
for i in range(N):

    # 타겟
    target = li[i]

    # 투포인터
    start_idx = 0
    end_idx = N - 1   # 음수를 고려해야하기 때문에 더 큰 값과 더해져 좋은 수가 될 수 도 있다.

    # 좋은 수 탐색
    while True:
        # 두 수가 만나면 종료
        if start_idx == end_idx:
            break

        # 좋은 수 확인
        elif li[start_idx] + li[end_idx] == target:
            
            if start_idx != i and end_idx != i:
                count += 1
                break

            elif start_idx == i:
                start_idx += 1

            elif end_idx == i:
                end_idx -= 1

        # 작은 경우
        elif li[start_idx] + li[end_idx] < target:
            start_idx += 1

        # 큰 경우
        else:
            end_idx -= 1
    
print(count)