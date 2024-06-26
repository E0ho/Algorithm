# 매일 다른 옷을 조합
# 각 종류별 최대 1가지 의상 착용
# 최소 한 개의 의상을 입는다.
from itertools import combinations

def solution(clothes):
    answer = 0
    
    # 사전
    dic = {}
    for i, k in clothes:
        li = dic.get(k, [])
        li.append(i)
        dic[k] = li
    
    total = 1
    for kind in dic.keys():
        total = (len(dic[kind]) + 1) * total
        
    answer = total - 1
    
    return answer









# 종류 별 item 수 사전
#     dic = {}
#     for item, kind in clothes:
#         dic[kind] = dic.get(kind, 0) + 1
    
#     # 0개 or 1개 선택
#     combi = 1
#     for value in dic.values():
#         # 하나씩 선택하는 경우의 수 + 하나도 안고르는 경우의 수
#         value += 1
#         combi *= value
    
#     # 모두 0인 경우 제거
#     answer = combi - 1