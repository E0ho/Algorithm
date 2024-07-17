# N 마리 포켓못 중 N/2 마리 선택
# 종류별 번호 (같은 종류 = 같은 번호)

def solution(nums):
    answer = 0
    
    # 포켓몬 수
    leng = len(nums)
    n = leng / 2
    
    dict = {}
    for num in nums:
        temp = dict.get(num, 0)
        dict[num] = temp + 1
    
    if len(dict) <= n:
        return len(dict)
    else:
        return n
    
    return answer









# 포켓몬 수
#     leng = len(nums)
    
#     # 포켓몬 종류 수
#     nums = set(nums)
    
#     # 가져갈 수 있는 포켓몬 종류
#     answer = min(len(nums), leng // 2)