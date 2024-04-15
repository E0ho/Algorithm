# 숫자 이어 붙여 소수 만들 수 있는 개수
from itertools import permutations

# 소수 판별
def is_prime(n):
    # 2 ~ (N-1) 나눠지는 수가 있으면 소수 아니다.
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True


def solution(numbers):
    answer = []
    li = list(numbers)
    
    # 전체 경우의 수
    total = set()
    
    # 모든 경우의 수 저장하기
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(li, i))
        for comb in temp:
            j = ""
            for i in comb:
                j += i
                
            j = int(j)
            if j != 1 and j != 0:
                total.add(j)
    
    # 모든 경우의 수 중 소수 판별하기
    for ele in total:
        if is_prime(int(ele)):
            answer.append(int(ele))
            
    return len(answer)