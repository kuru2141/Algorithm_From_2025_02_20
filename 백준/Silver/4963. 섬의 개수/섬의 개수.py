import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(x, y):
    global w, h
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > -1 and nx < w and ny > -1 and ny < h:
            if not visited[ny][nx] and arr[ny][nx]:
                visited[ny][nx] = 1
                dfs(nx, ny)

while True:
    w, h = map(int, input().split())

    if not w and not h:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0 for _ in range(w)] for _ in range(h)]

    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    cnt = 0

    for x in range(w):
        for y in range(h):
            if not visited[y][x] and arr[y][x]:
                visited[y][x] = 1
                cnt += 1
                dfs(x, y)

    print(cnt)