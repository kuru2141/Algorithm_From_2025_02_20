import heapq
import sys
input = sys.stdin.readline

def dijkstra(x):
    global M
    
    queue = []
    heapq.heappush(queue, (0, x))
    
    visited = [float('inf')] * (N + 1)
    visited[x] = 0

    while queue:
        new_w, new_x = heapq.heappop(queue)

        if visited[new_x] < new_w:
            continue
        
        for ele in arr[new_x]:
            if visited[ele[0]] >= new_w + ele[1]:
                visited[ele[0]] = new_w + ele[1]
                heapq.heappush(queue, (new_w + ele[1], ele[0]))

    return visited
            

N = int(input())
home = list(map(int, input().split()))

M = int(input())
arr = [[] for _ in range(M + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

result = [[] for _ in range(N + 1)]

for i in range(len(home)):
    visited = dijkstra(home[i])
    for j in range(len(visited)):
        result[j].append(visited[j])

for i in range(len(result)):
    result[i] = min(result[i])
print(result.index(sorted(set(result))[-2]))