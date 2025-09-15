import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(x, y, N, k):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < N and ny > -1 and ny < N:
            if visited[nx][ny] == 0:
                visited[nx][ny] = k
                dfs(nx, ny, N, k)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_height = max([max(arr[i]) for i in range(N)])

result = 0

for i in range(max_height + 1):
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if arr[x][y] <= i:
                visited[x][y] = -1

    k =0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0:
                k += 1
                visited[x][y] = k
                dfs(x, y, N, k)

    result = max(result, k)

print(result)