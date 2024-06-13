# 특정 프로세스 실행 순서
# Queue
# 우선순위가 높은 프로세스 

from collections import deque

def solution(priorities, location):
    answer = 0
    
    li = []
    for i, pri in enumerate(priorities):
        li.append((i, pri))
    
    q = deque(li)
    count = 0
    
    while True:
        
        i, pri = q.popleft()
        
        if pri == max(priorities):
            count += 1
            priorities.remove(pri)
            if i == location:
                return count
            
        else:
            q.append((i, pri))
        
        
        
    return answer



# # deque (idx, value)
#     priorities = deque(enumerate(priorities))
    
#     while True:
        
#         # 시작점
#         start = priorities[0][1]
        
#         # 최대값
#         max_value = max([x[1] for x in priorities])
        
#         # 시작점 우선순위가 가장 높은 경우 실행
#         if start == max_value:
#             target = priorities.popleft()
#             answer += 1
#             if target[0] == location:
#                 return answer

#         # 시작점 우선순위가 낮은 경우 회전
#         else:
#             priorities.rotate(-1)