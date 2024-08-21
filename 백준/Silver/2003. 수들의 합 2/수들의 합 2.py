# 입력
N, M = tuple(map(int, input().split()))
li = list(map(int, input().split()))

# 투포인터
start_index = 0
end_index = 0

sum_value = li[0]
count = 0

while True:
    
    # 값이 작다면
    if sum_value < M :
      end_index += 1
      if end_index == len(li):
          break
      sum_value += li[end_index]

    # 값이 크다면
    elif sum_value > M :
      sum_value -= li[start_index]
      start_index += 1

    # 값이 같다면
    else:
        count += 1
        end_index += 1
        if end_index == len(li):
          break
        sum_value += li[end_index]

print(count)