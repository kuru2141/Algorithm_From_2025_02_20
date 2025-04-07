import heapq
import sys
input = sys.stdin.readline

def dijkstra(x, N):
    queue = []
    heapq.heappush(queue, (1, x))

    while queue:
        new_w, new_x = heapq.heappop(queue)

        if new_x == N:
            print(new_w - 1)
            break

        for ele in arr[new_x]:
            if visited[ele[0]] > new_w + ele[1]:
                visited[ele[0]] = new_w + ele[1]
                heapq.heappush(queue, (new_w + ele[1], ele[0]))

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

visited = [float('inf')] * (N + 1)
visited[1] = 0

dijkstra(1, N)