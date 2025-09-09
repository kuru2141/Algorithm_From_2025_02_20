import sys
input = sys.stdin.readline

def dfs(x, y):
    global N, M, check

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < N and ny > -1 and ny < M:
            if arr[nx][ny] > arr[x][y]:
                check = 1
            
            if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
                visited[nx][ny] = 1
                dfs(nx, ny)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [-1, 1, 0 ,0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

result = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            check = 0
            visited[i][j] = 1
            dfs(i, j)
            if not check:
                result += 1
            
print(result)