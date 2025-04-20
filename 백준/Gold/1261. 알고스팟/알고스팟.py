import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

arr = [[int(e) for e in input().strip()] for _ in range(N)]
visited = [[float('inf') for _ in range(M)] for _ in range(N)]
visited[0][0] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

queue = [(0, 0, 0)]
while queue:
    cnt, r, c = heapq.heappop(queue)

    if r == N - 1 and c == M - 1:
        print(cnt)
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr > -1 and nr < N and nc > -1 and nc < M:
            if arr[nr][nc] == 1:
                new_cnt = cnt + 1
            else:
                new_cnt = cnt
            if visited[nr][nc] > new_cnt:
                visited[nr][nc] = new_cnt
                heapq.heappush(queue, (new_cnt, nr, nc))