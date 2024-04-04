# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 1. N개 숫자 입력받기
# 2. 반복문을 활용해 모든 숫자 더하기

# 입력
n = int(input())
string = input()
total = 0

# 모든 숫자 합
for ele in string:
    total += int(ele)

# 출력
print(total)