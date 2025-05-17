def solution(numbers):
    
    str_numbers = [str(ele) for ele in numbers]
    a = sorted(str_numbers, key = lambda x : x * 4, reverse=True)
    answer = ''.join(a)

    if not answer.lstrip('0'):
        return "0"
    
    return answer.lstrip('0')