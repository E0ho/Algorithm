# # 각 자리수 선택 (재귀)
# def choose(idx, answer, numbers, target, li):
    
#     # 종료 조건 (모든 원소를 사용)
#     if idx == len(numbers) + 1:
#         if sum(li) == target:
#             answer += 1
#         return

#     num = numbers[idx - 1]
#     li.append(num)
#     choose(idx, answer, numbers, target, li)
#     li.pop()
    
#     li.append(-num)
#     choose(idx, answer)
#     li.pop()
    
#     return



# choose(1, answer, numbers, target, li)

li = []
count = 0

def choose(numbers, index, target):
    global li, count
    
    if index == len(numbers) +1:
        if sum(li) == target:
            count += 1
        return
    
    num = numbers[index-1]
    li.append(num)
    choose(numbers, index + 1, target)
    li.pop()
    
    li.append(-num)
    choose(numbers, index + 1, target)
    li.pop()
    
def solution(numbers, target):
    global count
    index = 1
    
    choose(numbers, index, target)

    return count