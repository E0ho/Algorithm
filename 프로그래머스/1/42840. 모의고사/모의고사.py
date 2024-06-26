# 문제 찍기
# 1, 2, 3, 4, 5 /
# 2, 1, 2, 3, 2, 4 ,2, 5 /
# 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 /
def solution(answers):
    answer = []
    a = []
    b = []
    c = []
    
    # 찍는법
    a = [1, 2, 3, 4, 5] * (len(answers))
    b = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers))
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers))
    
    # print(a[:len(answers)])
    # print(b[:len(answers)])
    # print(c[:len(answers)])
    
    
    a_count, b_count, c_count = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a[i]:
            a_count += 1
            
        if answers[i] == b[i]:
            b_count += 1
            
        if answers[i] == c[i]:
            c_count += 1
    
    dic = {}
    dic[1] = a_count
    dic[2] = b_count
    dic[3] = c_count
    
    maxi = max(a_count, b_count, c_count)
    
    for key, item in dic.items():
        if item == maxi:
            answer.append(key)
            
    return answer





#     # 찍는 방법
#     a = [1, 2, 3, 4, 5] * (10000 // 5 + 1)
#     b = [2, 1, 2, 3, 2, 4 ,2, 5] * (10000 // 8 + 1)
#     c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (10000 // 10 + 1)
    
#     # 정답 개수
#     count = [[1, 0], [2, 0], [3, 0]]
    
#     # 정답 확인하기
#     for i in range(len(answers)):
#         if answers[i] == a[i]:
#             count[0][1] += 1
            
#         if answers[i] == b[i]:
#             count[1][1] += 1
            
#         if answers[i] == c[i]:
#             count[2][1] += 1
    
#     # 정답 개수로 정렬
#     count = sorted(count, key = lambda x : x[1])
#     count.reverse()
    
#     # 최대 값
#     max_count = count[0][1]
    
#     # 가장 많이 맞은 개수와 동일한 사람 저장
#     for key, ele in count:
#         if ele == max_count:
#             answer.append(key)
#         else:
#             break
            
#     answer.sort()