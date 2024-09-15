# DNA 문자열 - {A, C ,G ,T}
# 부분 문자열을 비밀번호로 사용
# < 조건 >
# 부분 문자열 길이 주어짐
# 각 문자의 최소 갯수 주어짐



def check(dic):
  for value in dic.values():
    if value > 0:
      return False

  return True

# 입력
s, p = tuple(map(int, input().split()))
li = list(input())
mini = list(map(int, input().split()))
min_dic = {
  'A' : 0, 
  'C' : 0, 
  'G' : 0, 
  'T' : 0
}
for key, value in zip(min_dic, mini):
  min_dic[key] = value


# 최초 부분문자열
for i in range(p):
  min_dic[li[i]] -= 1


count = 0
start_index = 0
end_index = p - 1
while True:

  # 부분 문자열 조건 검사
  if check(min_dic):
    count += 1

  # 윈도우 이동
  min_dic[li[start_index]] += 1
  start_index += 1
  end_index += 1

  if end_index == s:
    break

  min_dic[li[end_index]] -= 1

print(count)