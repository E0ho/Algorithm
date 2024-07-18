# 번호가 다른 번호의 접두어인 경우

def solution(phone_book):
    answer = True
    
    # 해시 사전 (시간 복잡도 감소)
    hash_dict = {}
    for number in phone_book:
        hash_dict[number] = True
    
    # 모든 번호 탐색
    for number in phone_book:
        s = ''
        for num in number:
            s += num
            if s in hash_dict and s != number:
                return False
            
            
    return answer















