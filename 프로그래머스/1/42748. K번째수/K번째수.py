def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])

    return answer







    # 명령어 반복
#     for cmd in commands:
#         i = cmd[0]
#         j = cmd[1]
#         k = cmd[2]
        
#         # 배열 슬라이싱
#         temp_array = array[i-1:j]
        
#         # 정렬
#         temp_array.sort()
        
#         # k 번째 원소 추가
#         answer.append(temp_array[k-1])
        