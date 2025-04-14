import heapq
import sys
input = sys.stdin.readline

cnt = 1
while True:
    N = int(input())
    if N == 0: break

    visited = [[float('inf') for _ in range(N)] for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]

    queue = [(0, 0, arr[0][0])]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    result = float('inf')

    while queue:
        r, c, w = heapq.heappop(queue)

        if r == N - 1 and c == N - 1:
            result = min(result, w)
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr > -1 and nr < N and nc > -1 and nc < N:
                new_w = w + arr[nr][nc]
                if visited[nr][nc] > new_w:
                    visited[nr][nc] = new_w
                    queue.append((nr, nc, new_w))
    
    print(f'Problem {cnt}: {result}')
    cnt += 1