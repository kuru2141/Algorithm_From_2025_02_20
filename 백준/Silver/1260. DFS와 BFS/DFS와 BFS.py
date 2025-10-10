from collections import deque
import sys
input = sys.stdin.readline

def dfs(V):
    for i in arr[V]:
        if not visited[i]:
            print(i, end = ' ')
            visited[i] = 1
            dfs(i)

def bfs(V):
    queue = deque()
    queue.append(V)
    
    while queue:
        x = queue.popleft()

        for i in arr[x]:
            if not visited[i]:
                print(i, end = ' ')
                queue.append(i)
                visited[i] = 1
    
N, M, V = map(int, input().split())

arr = [[] for _ in range(N + 1)]
arr[0].append(V)


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for ele in arr:
    ele.sort()

visited = [0 for _ in range(N + 1)]
visited[V] = 1
print(V, end = ' ')
dfs(V)

print()

visited = [0 for _ in range(N + 1)]
visited[V] = 1
print(V, end = ' ')
bfs(V)