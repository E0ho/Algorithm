# 한 사람만 완주 x
# participant : 참여한 선수 이름 리스트
# completion : 완주한 선수 이름 리스트
# 완주하지 못한 선수 출력

def solution(participant, completion):
    answer = ''
    
    # 참자가 hash
    participant_dic = {}
    for name in participant:
        num = participant_dic.get(name, 0)
        participant_dic[name] = num + 1
        
    # 완주자 제거
    for name in completion:
        participant_dic[name] = participant_dic[name] - 1
    
    # 완주하지 못한 이름 출력
    for key, value in participant_dic.items():
        if value != 0:
            answer += key
            
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