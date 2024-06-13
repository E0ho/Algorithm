# 한 사람만 완주 x
# participant : 참여한 선수 이름 리스트
# completion : 완주한 선수 이름 리스트
# 완주하지 못한 선수 출력
from collections import Counter

def solution(participant, completion):
    answer = ''
    a = Counter(participant)
    b = Counter(completion)

    a.subtract(b)
    
    a = list(a.most_common(1))
    
    answer = a[0][0]
    return answer



#     # 이름 순으로 정렬
#     participant.sort()
#     completion.sort()
    
#     # 가장 마지막 사람 초기 조건
#     answer = participant[-1]
    
#     # 참가자 -> 도착 했는지 확인
#     for i in range(len(completion)):
        
#         # 참가자가 완주자에 없는 경우
#         if participant[i] != completion[i]:
#             answer = participant[i]
#             break