from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]

    queue = deque()

    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
        queue.append((y, x))

    visited = [[0 for _ in range(M)] for _ in range(N)]

    cnt = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()
        
        if not visited[x][y]:
            cnt += 1
            visited[x][y] = 1

        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]

            if nr > -1 and nr < N and nc > -1 and nc < M and not visited[nr][nc] and arr[nr][nc]:
                visited[nr][nc] = 1
                queue.appendleft((nr, nc))

    print(cnt)