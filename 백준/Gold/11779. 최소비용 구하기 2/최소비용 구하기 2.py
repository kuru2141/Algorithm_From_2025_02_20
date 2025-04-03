import heapq
import sys
input = sys.stdin.readline

def dijkstra(x, y):
    visited = [float('inf')] * (n + 1)
    visited[x] = 0

    queue = []
    heapq.heappush(queue, (0, 1, x, [x]))

    while queue:
        now_w, cnt, now_x, visit_city = heapq.heappop(queue)

        if now_x == y:
            print(now_w)
            print(cnt)
            for city in visit_city:
                print(city, end = ' ')
            break

        for ele in arr[now_x]:
            if visited[ele[0]] <= now_w + ele[1]:
                continue
            visited[ele[0]] = now_w + ele[1]
            new_visit_city = visit_city + [ele[0]]
            heapq.heappush(queue, (now_w + ele[1], cnt + 1, ele[0], new_visit_city))

n = int(input())
m = int(input())

arr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

x, y = map(int, input().split())

dijkstra(x, y)