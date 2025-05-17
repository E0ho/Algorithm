# 총 N 마리 -> 절반을 가져가도 된다.
# 종류 마다 번호가 존재
# 포켓몬 종류 수 (최대)

# nums : [포켓몬 종류] (10,000)

def solution(nums):
    
    kind_set = set()
    N = len(nums)
    
    # 종류가 N/2 이상인 경우
    if len(set(nums)) > (N // 2) :
        return N // 2

    else:
        return len(set(nums))
    
    # answer = 0
    # return answer