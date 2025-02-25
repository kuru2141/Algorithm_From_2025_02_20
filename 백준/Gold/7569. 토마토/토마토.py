from collections import deque

N, M, H = map(int, input().split())

arr = []
queue = deque()

for _ in range(H):
    tmp_1 = []
    for _ in range(M):
        tmp_1.append(list(map(int, input().split())))
    arr.append(tmp_1)

for i in range(N):
    for j in range(M):
        for k in range(H):
            tmp = arr[k][j][i]
            if tmp == 1:
                queue.append((i, j, k, 0))

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

list_cnt = []

while queue:
    r, c, h, cnt = queue.popleft()
    
        
    for i in range(6):
        nr = r + dr[i]
        nc = c + dc[i]
        nh = h + dh[i]
    
        if nr > -1 and nr < N and nc > -1 and nc < M and nh > -1 and nh < H and arr[nh][nc][nr] == 0:
            queue.append((nr, nc, nh, cnt + 1))
            list_cnt.append(cnt + 1)
            arr[nh][nc][nr] = 1

result = 1
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][j][i] == 0:
                result = 0
if result:
    if list_cnt:
        print(max(list_cnt))
    else:
        print(0)
else:
    print(-1)