from collections import deque
import sys
input = sys.stdin.readline

def find_route(F_pos, J_pos, F_visited, J_visited, arr):
    global R, C
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    time = 1

    while J_pos:
        for _ in range(len(F_pos)):

            r, c = F_pos.popleft()

            for j in range(4):
                nr = r + dr[j]
                nc = c + dc[j]

                if nr > -1 and nr < R and nc > -1 and nc < C and (arr[nr][nc] != '#' and arr[nr][nc] != 'F') and not F_visited[nr][nc]:
                    F_visited[nr][nc] = 1
                    J_visited[nr][nc] = 1
                    F_pos.append((nr, nc))
                    
        for _ in range(len(J_pos)):
            r, c = J_pos.popleft()

            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                return time

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr > -1 and nr < R and nc > -1 and nc < C and not J_visited[nr][nc]:
                    if nr == 0 or nr == R - 1 or nc == 0 or nc == C - 1:
                        return time + 1
                    J_visited[nr][nc] = 1
                    J_pos.append((nr, nc))

        time += 1

    return 'IMPOSSIBLE'

R, C = map(int, input().split())

arr = []
F_visited = []
J_visited = []

for i in range(R):
    arr.append([e for e in input().strip()])
    F_visited.append([0 for _ in range(C)])
    J_visited.append([0 for _ in range(C)])

F_pos = deque()
J_pos = deque()

for i in range(R):
    for j in range(C):
        if arr[i][j] != '.':
            if arr[i][j] == 'F':
                F_pos.append((i, j))
                F_visited[i][j] = 1

            elif arr[i][j] == 'J':
                J_pos.append((i, j))
                
            J_visited[i][j] = 1

print(find_route(F_pos, J_pos, F_visited, J_visited, arr))