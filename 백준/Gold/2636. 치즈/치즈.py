from collections import deque

N, M = map(int, input().split())

arr = []
air_arr = []

air_queue = deque()

for _ in range(N):
    arr.append(list(map(int, input().split())))
    air_arr.append([0 for _ in range(M)])

air_arr[0][0] = -1

time = -1
melt_cheeze = deque()
d_cheeze = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while True:
    if melt_cheeze:
        d_cheeze = len(melt_cheeze)
        while melt_cheeze:
            r, c = melt_cheeze.pop()
            air_arr[r][c] = -1
            arr[r][c] = 0
    else:
        if time != -1:
            print(time)
            print(d_cheeze)
            break
        
    visited = []
    air_queue.append((0, 0))

    for _ in range(N):
        visited.append([False for _ in range(M)])
    visited[0][0] = True
    
    while air_queue:
        r, c = air_queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr > -1 and nr < N and nc > -1 and nc < M and not visited[nr][nc] and arr[nr][nc] == 0:
                visited[nr][nc] = True
                air_arr[nr][nc] = -1
                air_queue.append((nr, nc))
    
    cheeze_arr = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cheeze_arr.append((i, j))
    
    while cheeze_arr:
        r, c = cheeze_arr.pop()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr > -1 and nr < N and nc > -1 and nc < M and air_arr[nr][nc] == -1:
                melt_cheeze.append((r, c))
                break
            
    time += 1