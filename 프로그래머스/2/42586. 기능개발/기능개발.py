# 기능 개선 작업
# 각 기능이 진도 100% 일때 서비스 반영
# 앞에 있는 기능이 배포될때 까지 뒤는 대기

from collections import deque
def solution(progresses, speeds):
    answer = []
    
    # 프로세스 Queue
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # 각 프로세스 진행
    while progresses:
        
        # 각 프로세스 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
            
        count = 0
        
        # 첫번째 프로세스 종료 시, 이어지는 완료된 모든 프로세스 종료
        while progresses[0] >= 100:
            temp = progresses.popleft()
            speeds.popleft()
            count += 1
            
            if not progresses:
                break
        
        if count != 0:
            answer.append(count)
        
    return answer













    
#     progresses = deque(progresses)
#     speeds = deque(speeds)

    
    
#     while len(progresses) > 0:

#         # 오늘 배포할 작업 수
#         count = 0
        
#         # 작업 진행
#         for idx, value in enumerate(speeds):
#             progresses[idx] += value
        
#         # 배포할 수 있는 작업 수 확인 
#         while progresses[0] >= 100:
#             count += 1
#             progresses.popleft()
#             speeds.popleft()
            
#             if len(progresses) == 0:
#                 break

#         if count:
#             answer.append(count)