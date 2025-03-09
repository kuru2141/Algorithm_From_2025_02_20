from collections import deque

def dfs(v):
    for ele in graph[v]:
        if not visited[ele]:
            print(ele, end = ' ')
            visited[ele] = 1
            dfs(ele)
    

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
graph[0].append(V)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for ele in graph:
    ele.sort()

visited = [0] * (N + 1)
visited[0] = 1

dfs(0)
print()

queue = deque()
queue.append(0)

visited = [0] * (N + 1)
visited[0] = 1

while queue:
    v = queue.popleft()
    for ele in graph[v]:
        if not visited[ele]:
            print(ele, end = ' ')
            visited[ele] = 1
            queue.append(ele)
