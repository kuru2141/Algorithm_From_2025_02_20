import sys
input = sys.stdin.readline

def dfs(r, c, select):
    global result, R, C

    if len(select) == 26 or len(select) == R * C:
        result = max(result, len(select))
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr > -1 and nr < R and nc > -1 and nc < C:
            if not visited[nr][nc]:
                if arr[nr][nc] in select:
                    result = max(result, len(select))
                    continue
                
                visited[nr][nc] = 1
                dfs(nr, nc, select + arr[nr][nc])
                visited[nr][nc] = 0

R, C = map(int, input().split())
arr = [[e for e in input().strip()] for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited = [[0 for _ in range(C)] for _ in range(R)]
visited[0][0] = 1

result = 0

dfs(0, 0, arr[0][0])

print(result)