# 한 번호가 다른 번호의 접두어인 경우가 있는지 확인

# phone_book : [전화번호]

# 접두어가 있는 경우 False
def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    answer = True
    return answer