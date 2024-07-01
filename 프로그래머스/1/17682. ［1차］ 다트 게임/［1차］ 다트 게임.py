# 3판

# 점수 : 1 ~ 10
# 지수 : single, double, triple

# [옵션]
# 스타상 : 이전 값, 현재 값 2배
# 아차상 : 현재 값 음수로 변환



# 이전 수와 다음 수를 확인 -> 0, 1, 10 분류
def check_num(dartResult, ele, i):
        
    # 1 vs 10
    if ele == '1':
        if dartResult[i + 1] == '0': 
            return '10'                 # 10
        else:
            return '1'                  # 1
        
    # 0 vs 10
    elif ele == '0':     
        if dartResult[i - 1] == '1': 
            return -1                   # 10
        else: 
            return 0                    # 0
        
    else:
        return ele
        
        
def solution(dartResult):

    answer = 0
    score = []
    
    # 지수 매핑
    pow_dic = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    
    for i, ele in enumerate(dartResult):
        
        # 점수 확인
        if ele.isdigit():
            ele = check_num(dartResult, ele, i)    # 숫자 확인 (10)
            if ele == -1:                          # 0이 10으로 사용된 경우
                continue
                
            score.append(int(ele))
        
        # 지수 확인
        elif ele.isalpha():
            score[-1] = score[-1] ** pow_dic[ele]   # 지수 승
        
        
        # [옵션]
        else:
            if ele == '*':
                if len(score) > 1:
                    score[-2] = score[-2] * 2       # 이전 값 2배
                    
                score[-1] = score[-1] * 2           # 현재 값 2배
                
            # '#' 옵션
            else:
                score[-1] = score[-1] * -1           # 현재 값 음수
                

    # 모든 합
    answer = sum(score)
    return answer