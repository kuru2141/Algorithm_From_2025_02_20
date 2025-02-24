from collections import deque

def check_tomato(arr):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return 1
    return 0

M, N = map(int, input().split())

arr = []
visited = []
queue = deque()

for _ in range(N):
    arr.append(list(map(int, input().split())))
    visited.append([False for _ in range(M)])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j, 0))
            visited[i][j] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

list_cnt = []

while queue:
    r, c, cnt = queue.popleft()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr > -1 and nr < N and nc > -1 and nc < M and not arr[nr][nc] and not visited[nr][nc]:
            queue.append((nr, nc, cnt + 1))
            list_cnt.append(cnt + 1)
            arr[nr][nc] = 1
            
if check_tomato(arr):
    print(-1)
else:
    if list_cnt:
        print(max(list_cnt))
    else:
        print(0)