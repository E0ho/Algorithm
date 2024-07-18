def solution(clothes):
    answer = 0
    
    # 해시 사전
    hash_dict = {}
    for value, kind in clothes:
        li = hash_dict.get(kind, [])
        li.append(value)
        hash_dict[kind] = li
    
    
    # 각 종류 별 갯수
    num_dict = {}
    for key, value in hash_dict.items():
        num_dict[key] = len(hash_dict[key])
    
    # 총 경우의 수
    count = 1
    for _, value in num_dict.items():
        count = count * (value + 1)
    
    answer = count - 1   # 모두 선택하지 않은 경우
    return answer