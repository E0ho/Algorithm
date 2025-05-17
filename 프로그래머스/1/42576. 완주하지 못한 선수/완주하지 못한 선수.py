# participant : 참가한 선수들의 이름 (100,000)
# completion : 완주한 선수들의 이름

def solution(participant, completion):
    dic = {}
    for key in participant:
        if dic.get(key, False):
            dic[key] += 1
        else:
            dic[key] = 1
    
    for key in completion:
        dic[key] -= 1
    
    new_dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    print(new_dic[0][0])
    answer = new_dic[0][0]
    
    return answer