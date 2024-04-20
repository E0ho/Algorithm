# (1, 1) -> (n, n)
# 동 서 남 북
# 상대 진영으로 가는 가장 빠른 방법
# 도착 불가 시 -1


from collections import deque



def solution(maps):
    
    # 범위 내
    def in_range(r, c):
        return 0 <= r and 0 <= c and r < n and c < m

    
    def bfs():
        while q:
            r, c = q.popleft()
            count = visited[r][c]
            
            # 도착
            if r == n-1 and c == m -1:
                return count
            
            for dr, dc in zip(drs, dcs):
                nr = r + dr
                nc = c + dc
                
                # 격자 범위 / 방문 여부 / 벽 여부
                if in_range(nr, nc) and visited[nr][nc] == 0 and maps[nr][nc] == 1:
                    q.append((nr, nc))
                    visited[nr][nc] = count + 1

        return (-1)
        
    answer = -1
    
    # dx, dy (남, 동, 북, 서)
    drs = [1, 0, -1, 0]
    dcs = [0, 1, 0, -1]
    
    # 초기 값
    r, c = 0, 0
    n = len(maps)     # 행
    m = len(maps[0])  # 열
    
    # Visited
    visited = [
        [0] * m
        for _ in range(n)
    ] 
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    answer = bfs()
    
    
    return answer