from collections import deque
import copy

def check_area(arr):
    queue = deque()
    
    dic = dict()
    visited = []

    for _ in range(N):
        visited.append([False for _ in range(N)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            
            visited[i][j] = True
            queue.appendleft((i, j, arr[i][j]))
                
            while queue:
                r, c, color = queue.popleft()

                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]

                    if nr > -1 and nr < N and nc > -1 and nc < N and visited[nr][nc] == False and color == arr[nr][nc]:
                        queue.append((nr, nc, color))
                        visited[nr][nc] = True

            cnt += 1
    return cnt


N = int(input())

arr = []

for _ in range(N):
    arr.append([ele for ele in input()])
tmp_no = check_area(arr) # 비적녹색약인 사람이 볼 수 있는 구역 


for i in range(N):
    for j in range(N):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

tmp_yes = check_area(arr) # 적녹색약인 사람이 볼 수 있는 구역 


print(tmp_no, tmp_yes)