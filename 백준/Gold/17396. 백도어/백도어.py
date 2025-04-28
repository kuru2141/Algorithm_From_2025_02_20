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

        if visited[new_x] < new_w:
            continue
        
        for ele in arr[new_x]:
            if visited[ele[0]] > new_w + ele[1] and (not sight[ele[0]] or ele[0] == y):
                heapq.heappush(queue, (new_w + ele[1], ele[0]))
                visited[ele[0]] = new_w + ele[1]

    return -1

N, M = map(int, input().split())
visited = [float('inf')] * N
arr = [[] for _ in range(N)]

sight = list(map(int, input().split()))

for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

print(dijkstra(0, N - 1))