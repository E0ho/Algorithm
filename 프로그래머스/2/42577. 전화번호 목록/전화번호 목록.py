# 번호가 다른 번호의 접두어인 경우

def solution(phone_book):
    answer = True
    
    n = len(phone_book)
    
    # 문자 개수로 정렬
    phone_book.sort(key = len)
    
    # 사전 만들기
    dic = {}
    for number in phone_book:
        dic[number] = number
    
    # 접두어 확인
    for number in phone_book:
        s = ""
        for num in number:
            s += num
            if s in dic.keys() and s != number:
                answer = False
                return answer
        
    return answer















