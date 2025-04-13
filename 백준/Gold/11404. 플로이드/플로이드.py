import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]
visited = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    visited[a][b] = min(visited[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if visited[i][j] == float('inf'):
            print(0, end = ' ')
        else:
            print(visited[i][j], end = ' ')
    print()