# LZW 무손실 압축

# 모든 알파벳 사전 초기화
# 입력에서 일치하는 가장 긴 문자열 찾기 // w -> Index 출력
# 출력된 문자열 현재 입력에서 제거
# 출력되지 못한 문자열 사전에 추가

from collections import deque
def solution(msg):
    answer = []
    
    # 사전 만들기
    word_dic = {}
    for i in range(1, 27):
        word_dic[chr(64 + i)] = i     # 'A' == 65 / 'Z' == 90
    
    # 문자 Queue
    q = deque(msg)
    
    # 가능한 최대 문자 찾기
    temp_word = ''
    word = ''
    while q:
        temp = q.popleft()
        temp_word += temp

        if temp_word in word_dic:
            temp_index = word_dic[temp_word]

        else:
            word_dic[temp_word] = len(word_dic) + 1
            answer.append(temp_index)
            q.appendleft(temp)
            temp_word = ''
            
    answer.append(temp_index)
    return answer