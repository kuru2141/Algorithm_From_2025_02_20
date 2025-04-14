import sys
input = sys.stdin.readline

V, E = map(int, input().split())

arr = [tuple(map(int, input().split())) for _ in range(E)]
visited = [[float('inf') for _ in range(V + 1)] for _ in range(V + 1)]

for a, b, c in arr:
    visited[a][b] = min(visited[a][b], c)

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

result = float('inf')
for i in range(1, V + 1):
    for j in range(1, V + 1):
        if i == j:
            result = min(result, visited[i][j])

if result == float('inf'):
    print(-1)
else:
    print(result)