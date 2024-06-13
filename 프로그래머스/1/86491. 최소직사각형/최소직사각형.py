# 지갑의 크기
# 모든 명함을 수납할 수 있는 최소 크기의 지갑
# 가로, 세로 길이
def solution(sizes):
    answer = 0
    
    for size in sizes:
        size.sort()
    
    width = max([x[0] for x in sizes])
    height = max([x[1] for x in sizes])
    
    answer = (width * height)

    return answer




#     # 가로 길이를 무조건 긴변으로 돌리기
#     li = []
#     for a, b in sizes:
#         li.append( (max(a, b), min(a, b)) )
        
#     width_li = []
#     height_li = []
    
#     # 가로 세로 배열 만들기
#     for width, height in li:
#         width_li.append(width)
#         height_li.append(height)
    
#     # 각 길이의 최대 값
#     answer = max(width_li) * max(height_li)