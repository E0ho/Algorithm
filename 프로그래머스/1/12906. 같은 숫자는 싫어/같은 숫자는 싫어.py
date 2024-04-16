# 0 ~ 9
# 연속적으로 나타나는 숫자는 하나만 남기고 제거

from collections import deque

def solution(arr):
    answer = []
    
    # 초기값 (첫번째 원소)
    pre_value = arr[0]
    answer.append(pre_value)
    
    # 모든 원소 검사
    for now_value in arr:
        
        # 중복되지 않는 원소 추가
        if pre_value != now_value:
            answer.append(now_value)
        
        pre_value = now_value
        
    return answer