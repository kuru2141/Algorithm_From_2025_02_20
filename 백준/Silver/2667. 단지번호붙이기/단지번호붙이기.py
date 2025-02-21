from collections import deque

N = int(input())

arr = []

for _ in range(N):
    arr.append([int(e) for e in input()])

queue = deque()
visited = []
for _ in range(N):
    visited.append([False for _ in range(N)])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 1
list_home = []

for i in range(N):
    for j in range(N):
        if visited[i][j] or arr[i][j] == 0: continue
        visited[i][j] = True
        queue.appendleft((i, j, arr[i][j]))
        tmp = 1
        
        while queue:
            r, c, num = queue.popleft()
            arr[i][j] = cnt
            
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if nr > -1 and nr < N and nc > -1 and nc < N and num == arr[nr][nc] and not visited[nr][nc]:
                    queue.appendleft((nr, nc, arr[nr][nc]))
                    visited[nr][nc] = True
                    arr[nr][nc] = cnt
                    tmp += 1
        list_home.append(tmp)
        cnt += 1

list_home.sort()
print(cnt - 1)

for ele in list_home:
    print(ele)