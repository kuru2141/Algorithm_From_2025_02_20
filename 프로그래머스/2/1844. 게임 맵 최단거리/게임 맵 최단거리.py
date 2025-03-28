def solution(maps):
    from collections import deque
    
    N = len(maps)
    M = len(maps[0])
    
    visited = []
    queue = deque()
    
    for _ in range(N):
        visited.append([False for _ in range(M)])
    visited[0][0] = True
    queue.append((0, 0, 1))
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    list_result = []
    
    while queue:
        r, c, cnt = queue.popleft()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr > -1 and nr < N and nc > -1 and nc < M and not visited[nr][nc] and maps[nr][nc] != 0:
                if nr == N - 1 and nc == M - 1:
                    list_result.append(cnt + 1)
                    break
                queue.append((nr, nc, cnt + 1))
                visited[nr][nc] = True
    
    if not list_result:
        answer = -1
    else:
        answer = min(list_result)
        
    return answer