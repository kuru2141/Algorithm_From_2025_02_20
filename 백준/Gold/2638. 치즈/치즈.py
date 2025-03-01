from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

cheeze = []
for i in range(N): # 치즈의 좌표를 cheeze에 담음
    for j in range(M):
        if arr[i][j] == 1:
            cheeze.append((i, j))

air_queue = deque()

melt_cheeze = deque()
melt_cheeze.append((0, 0))

time = -1 # 제거를 새로운 루프로 들어갈 때 하기 때문에 time이 하나 더 세짐

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while melt_cheeze: # 녹는 치즈가 하나도 없다면 종료
    while melt_cheeze: # 녹는 치즈가 있다면, 해당 치즈를 arr에서 없앰
        r, c = melt_cheeze.pop()
        if r != 0 and c != 0:
            cheeze.remove((r, c))
            arr[r][c] = 0

    visited = []
    for _ in range(N): # 외부 공기 탐색을 위한 visited
        visited.append([False for _ in range(M)])
    visited[0][0] = True
    
    air = [[False for _ in range(M)] for _ in range(N)] # 외부 공기 좌표를 모아둔 배열
    air[0][0] = True

    air_queue.append((0, 0))

    while air_queue: # 외부 공기 탐색 (BFS)
        r, c = air_queue.pop()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr > -1 and nr < N and nc > -1 and nc < M and not arr[nr][nc] and not visited[nr][nc]:
                air_queue.append((nr, nc))
                air[nr][nc] = True
                visited[nr][nc] = True
                
    for x in range(len(cheeze)): # 치즈와 맞닿은 외부 공기가 2개 이상 있을 시, 제거 대상
        r, c = cheeze[x]

        cnt = 0
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr > -1 and nr < N and nc > -1 and nc < M and air[nr][nc]:
                cnt += 1

        if cnt > 1:
            melt_cheeze.append((r, c))

    time += 1

print(time)