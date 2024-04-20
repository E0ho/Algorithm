# 네트워크 -> 연결된 PC
# 네트워크 개수 구하기

from collections import deque

def solution(n, computers):
    answer = 0

    def bfs():
        while q:
            vertex = q.popleft()
            
            for v in li[vertex]:
                if visited[v] == 0:
                    q.append(v)
                    visited[v] = count

    
    # 리스트로 만들기
    li = [[] for _ in range(n)]       # computer
    visited = [0 for _ in range(n)]   # 방문
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                li[i].append(j)
    
    # bfs 탐색
    q = deque()
    
    # 출발점

    count = 0

    for i in range(n):
        if visited[i] == 0:
            count += 1
            q.append(i)
            visited[i] = count
            bfs()
    
    print(visited)
    answer = max(visited)
    
    return answer