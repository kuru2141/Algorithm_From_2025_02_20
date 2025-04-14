import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[float('inf') for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            visited[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])

for i in range(N):
    for j in range(N):
        if visited[i][j] == float('inf'):
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print('')