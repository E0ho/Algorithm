def solution(s):
    answer = True
    
    count = 0
    
    for c in s:
        # 괄호 열림
        if c == '(':
            count += 1
            
        # 괄호 닫힘
        else:
            count -= 1
        
        # 열리지 않고 닫힌 경우
        if count < 0:
            answer = False
            return answer
    # 개수가 맞지 않은 경우
    if count != 0:
        answer = False

    return answer