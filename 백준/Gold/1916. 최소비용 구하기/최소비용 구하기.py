import heapq
import sys
input = sys.stdin.readline

def dijkstra(x, y):
    queue = []
    heapq.heappush(queue, (0, x))

    while queue:
        new_w, new_x = heapq.heappop(queue)

        if new_x == y:
            return new_w

        for ele in arr[new_x]:
            if visited[ele[0]] <= new_w + ele[1]:
                continue
            visited[ele[0]] = new_w + ele[1]
            heapq.heappush(queue, (new_w + ele[1], ele[0]))

N = int(input())
M = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

x, y = map(int, input().split())

visited = [float('inf')] * (N + 1)
visited[x] = 1

print(dijkstra(x, y))