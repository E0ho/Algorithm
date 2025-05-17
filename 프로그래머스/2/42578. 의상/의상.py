# 최소 1개 이상 옷 입음
# 종류별 하나 선택 가능

def solution(clothes):
    dic = {}
    
    # 각 종류 별, 의상 개수
    for name, kind in clothes:
        dic[kind] = dic.get(kind, 0) + 1
    
    total = 1
    for cnt in dic.values():
        total *= (cnt + 1)
    
    return total - 1