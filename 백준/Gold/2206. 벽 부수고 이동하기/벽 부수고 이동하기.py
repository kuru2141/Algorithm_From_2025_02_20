from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[int(e) for e in input().strip()] for _ in range(N)]

visited = [[float('inf')] * len(arr[0]) for _ in range(len(arr))]
visited_br = [[float('inf')] * len(arr[0]) for _ in range(len(arr))]

visited[0][0] = 1

queue = deque()
queue.append((0, 0, 0, 1))

dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

result = float('inf')

while queue:
    r, c, br, cnt = queue.popleft()

    if r == N - 1 and c == M - 1:
        result = cnt
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr > - 1 and nr < N and nc > -1 and nc < M:
            if arr[nr][nc] == 0:
                if not br:
                    if visited[nr][nc] > cnt + 1:
                        queue.append((nr, nc, br, cnt + 1))
                        visited[nr][nc] = cnt + 1
                else:
                    if visited_br[nr][nc] > cnt + 1:
                        queue.append((nr, nc, br, cnt + 1))
                        visited_br[nr][nc] = cnt + 1
            else:
                if not br:
                    queue.append((nr, nc, 1, cnt + 1))
                    visited_br[nr][nc] = cnt + 1
                    
if result == float('inf'):
    print(-1)
else:
    print(result)