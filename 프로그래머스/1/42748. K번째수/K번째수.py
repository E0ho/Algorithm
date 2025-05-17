# i ~ j (INDEX - 1)
# K 번째 수 (INDEX - 1)

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp_array = array[i-1:j]
        temp_array.sort()
        answer.append(temp_array[k-1])

    return answer