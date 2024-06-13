# 스코빌 지수 k이상으로 만들기
# 가장 낮은 두개의 음식을 섞기 
# (가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 스코빌 지수가 K이상일때 까지 섞기
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    count = 0
    while True:
        
        if scoville[0] >= K:
            break
        
        if len(scoville) == 1:
            return -1
        
        count += 1
        mini = heapq.heappop(scoville)
        mini2 = heapq.heappop(scoville)

        temp = mini + (2 * mini2)

        heapq.heappush(scoville, temp)
        
    answer = count
    return answer




#     # 최소 힙으로 변환
#     heapq.heapify(scoville)
    
#     # 반복
#     while True:
        
#         # 모든 음식의 스코빌 지수 K 이상 -> 종료
#         if scoville[0] >= K:
#             return answer
        
#         # 모든 음식의 스코빌 지수 k 이상 불가
#         if len(scoville) == 1:
#             return -1
        
#         # 음식 섞기
#         answer += 1
#         first = heapq.heappop(scoville)
#         second = heapq.heappop(scoville)

#         cal = first + (second * 2)
#         heapq.heappush(scoville, cal)