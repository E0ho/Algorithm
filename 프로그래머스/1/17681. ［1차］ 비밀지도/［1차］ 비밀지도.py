# 비밀 지도 (암호화)

# N 정사각형 지도 2개 겹쳐서 지도 확인
# 길 : 0 -> " "
# 벽 : 1 -> "#"
# 10진수 -> 2진수

from collections import deque

def solution(n, arr1, arr2):
    answer = []
    
    # 지도
    map = []
    
    # 10진수 -> 2진수로 변환
    for num1, num2 in zip(arr1, arr2):
        
        # 지도 1        
        q1 = deque()   
        
        # 2진수로 변환
        for i in range(n):
            temp = num1 % 2
            q1.appendleft(temp)
            
            num1 = num1 // 2
            if num1 == 1:
                q1.appendleft(1)
                break
        
        # 0으로 채우기
        while len(q1) != n:
            q1.appendleft(0)
        
        #########################################
        
        # 지도 2        
        q2 = deque()   
        
        # 2진수로 변환
        for i in range(n):
            temp = num2 % 2
            q2.appendleft(temp)
            
            num2 = num2 // 2
            if num2 == 1:
                q2.appendleft(1)
                break
        
        # 0으로 채우기
        while len(q2) != n:
            q2.appendleft(0)
                
                
        #########################################
        
        # 두 지도 겹치기
        s = ''
        for a, b in zip(q1, q2):
            if a == 1 or b == 1:
                s += '#'
            else:
                s += " "
        
        map.append(s)
        
    print(map)  
    answer = map
                
    return answer