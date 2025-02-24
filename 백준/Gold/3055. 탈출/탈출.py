from collections import deque

def check_water(water, arr):
    global dr, dc, R, C
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                water.append((i, j))

    while water:
        a, b = water.popleft()
        for w in range(4):
            na = a + dr[w]
            nb = b + dc[w]

            if na > -1 and na < R and nb > -1 and nb < C and (arr[na][nb] == '.' or arr[na][nb] == 'S'):
                arr[na][nb] = '*'
    return

R, C = map(int, input().split())

arr = []
visited = []
check_visited = []
water = deque()
back_cnt = 0

for _ in range(R):
    arr.append([e for e in input()])

for i in range(R):
    tmp = []
    for j in range(C):
        if arr[i][j] != '.' and arr[i][j] != 'D':
            if arr[i][j] == 'S':
                a, b = i, j
            tmp.append(True)
        else:
            if arr[i][j] == 'D':
                x, y = i, j
            tmp.append(False)
    visited.append(tmp)

for i in range(R):
    tmp = []
    for j in range(C):
        if arr[i][j] != 'D':
            tmp.append(True)
        else:
            tmp.append(False)
    check_visited.append(tmp)

queue = deque()
queue.append((a, b, 0))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

list_result = []

while queue:
    r, c, cnt = queue.popleft()

    if back_cnt < cnt:
        check_water(water, arr)
    back_cnt = cnt

    if arr[r][c] == '*':
        continue
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr > -1 and nr < R and nc > -1 and nc < C and not visited[nr][nc] and arr[nr][nc] != '*':
            if nr == x and nc == y:
                list_result.append(cnt + 1)
                break
            queue.append((nr, nc, cnt + 1))
            visited[nr][nc] = True

if not list_result:
    print('KAKTUS')
else:
    print(min(list_result))