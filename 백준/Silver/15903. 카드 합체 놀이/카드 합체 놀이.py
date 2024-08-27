# N 장의 카드 중 m번 합체
# x = x + y
# y = x + y
# 점수를 가장 작게 만들기

# 입력
n, m = tuple(map(int, input().split()))
li = list(map(int, input().split()))

for _ in range(m):

  li.sort()
  temp = li[0] + li[1]
  li[0] = temp
  li[1] = temp
  
print(sum(li))