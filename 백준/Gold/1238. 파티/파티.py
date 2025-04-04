import heapq
import sys
input = sys.stdin.readline

def dijkstra(X, i, idx):
    global result
    
    queue = []
    heapq.heappush(queue, (0, X))

    visited = [float('inf')] * (N + 1)
    visited[X] = 0

    while queue:
        new_w, new_x = heapq.heappop(queue)

        if new_x == i:
            result[idx] += new_w
            break

        for ele in arr[new_x]:
            if visited[ele[0]] < ele[1] + new_w:
                continue
            visited[ele[0]] = ele[1] + new_w
            heapq.heappush(queue, (visited[ele[0]], ele[0]))

N, M, X = map(int, input().split())
arr = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y, t = map(int, input().split())
    arr[x].append((y, t))

result = [0] * (N + 1)

for i in range(1, N + 1):
    dijkstra(X, i, i)
    dijkstra(i, X, i)

print(max(result))