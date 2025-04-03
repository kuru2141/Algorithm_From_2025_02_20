import heapq
import sys
input = sys.stdin.readline

def dijkstra(m, x):
    queue = []
    heapq.heappush(queue, (m, x))
    
    visited[x] = 0

    while queue:
        now_m, now_x = heapq.heappop(queue)

        for ele in arr[now_x]:
            if visited[ele[0]] <= now_m + ele[1]:
                continue
            visited[ele[0]] = now_m + ele[1]
            heapq.heappush(queue, (now_m + ele[1], ele[0]))
        

n, m, r = map(int, input().split())
item = [0] + list(map(int, input().split()))

arr = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    arr[a].append((b, l))
    arr[b].append((a, l))

result = 0

for i in range(1, n + 1):
    visited = [float('inf')] * (n + 1)
    dijkstra(0, i)

    total_item = 0
    for i in range(1, n + 1):
        if visited[i] <= m:
            total_item += item[i]
    result = max(result, total_item)

print(result)