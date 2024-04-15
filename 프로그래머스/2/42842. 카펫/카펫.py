# 중앙 노란색
# 테두리 1줄 갈색
# 갈색 수, 노란색 수 -> 카펫의 가로, 세로 크기 (가로 >= 세로)

def solution(brown, yellow):
    answer = []
    
    # 넓이
    total = brown + yellow
    
    # 가로 * 세로 = 넓이
    for i in range(1, total):
        if total % i == 0:
            a = i
            b = total // i
            
            # 가로가 더 길어진 경우
            if a >= b:
                if (a - 2) * (b - 2) == yellow:
                    # 노란색을 둘러싸야 한다.
                    answer = [a, b]
                    return answer
            
    return answer