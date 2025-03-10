from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [0] * 101
visited = [float('inf')] * 101

for _ in range(M + N):
    x, y = map(int, input().split())
    graph[x] = y

queue = deque()
queue.append((1, 0))

dr = [1, 2, 3, 4, 5, 6]

while queue:
    r, c = queue.popleft()
    if r == 100:
        print(c)
        break

    for i in range(6):
        nr = r + dr[5 - i]
        if nr < 101 and visited[nr] > c + 1:
            if graph[nr]:
                if visited[graph[nr]] > c + 1:
                    queue.append((graph[nr], c + 1))
                
            else:
                queue.append((nr, c + 1))
                visited[nr] = c + 1