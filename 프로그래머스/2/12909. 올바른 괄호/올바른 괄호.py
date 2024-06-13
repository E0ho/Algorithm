from collections import deque

def solution(s):
    answer = True
    
    q = deque()
    
    for ele in s:
        if ele =='(':
            q.append('(')
    
        if ele ==')':
            if not q:
                return False
            
            temp = q.popleft()
            
            if temp != '(':
                return False
            
    if q:
        return False

    return answer