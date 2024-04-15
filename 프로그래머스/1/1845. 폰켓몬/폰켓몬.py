# n 마리 포켓몬 중 n/2 가져가도 좋다
# 포켓몬 종류 별 고유 번호 (같은 종류 같은 번호)
# 포켓몬 종류 최대로 가져가기

def solution(nums):
    answer = 0
    
    # 포켓몬 수
    leng = len(nums)
    
    # 포켓몬 종류 수
    nums = set(nums)
    
    # 가져갈 수 있는 포켓몬 종류
    answer = min(len(nums), leng // 2)
        
    return answer