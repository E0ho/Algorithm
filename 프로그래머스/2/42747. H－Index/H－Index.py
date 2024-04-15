# 과학자의 생산성과 영향력을 나타내는 지표
# h 번 이상 인용된 논문이 h편 이상 
# h 번 이하 인용된 논문이 h편 이하
# h의 최댓값

def solution(citations):
    answer = 0
    
    # 인용 수 정렬 (최대값을 구하기 위해)
    citations.sort(reverse = True)
    
    # 논문 인용 수 < 이상인 논문 수
    # 논문 인용 수 > 이하인 논문 수
    for num in range(max(citations), -1, -1):
        
        count = 0        # 이상인 논문 개수
        rest = 0         # 이하인 논문 개수
        
        for ele in citations:
            
            # 높은 경우
            if ele >= num:
                count += 1
                
            # 낮은 경우
            elif ele < num:
                rest += 1
        
        if count >= num and rest <= num:
            answer = num
            break
    
    return answer